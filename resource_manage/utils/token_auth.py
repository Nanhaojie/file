from calendar import timegm
from datetime import datetime, timedelta

import jwt

from rest_framework_jwt.authentication import JSONWebTokenAuthentication, jwt_decode_handler
from django.utils.translation import ugettext as _
from rest_framework import exceptions
from rest_framework_jwt.settings import api_settings
from django_redis import get_redis_connection
from django.conf import settings
from user.models import AccountModel

redis_conn = get_redis_connection('login_user')


class SlideTokenAuthentication(JSONWebTokenAuthentication):

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """
        jwt_key = self.get_jwt_value(request)
        if jwt_key is None:
            return None
        user_info = redis_conn.get(jwt_key)
        # 没有user_info 说明已经被挤掉或者登录超时
        if not user_info:
            msg = _('登录失效')
            raise exceptions.AuthenticationFailed(msg)
        user_info = eval(redis_conn.get(jwt_key))
        if user_info.get('openid'):
            return self.applet_check(jwt_key, user_info)
        else:
            return self.bkd_check(jwt_key, user_info)


    def applet_check(self, jwt_key, user_info):
        user = AccountModel.objects.filter(open_id= user_info['openid']).first()
        if not user:
            msg = _('用户不存在')
            raise exceptions.AuthenticationFailed(msg)
        jwt_value = user_info['token']
        # 检查是否过期
        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            # 已过期，滑动重置
            user_info = {
                'openid': user_info['openid'],
                'session_key': user_info['session_key'],
                'exp': datetime.timestamp(datetime.now() + timedelta(minutes=settings.TOKEN_EXP))
            }
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            # payload = jwt_payload_handler(user_info)
            payload = self.my_jwt_payload_handler(user_info)
            token = jwt_encode_handler(payload)
            val = {"token": token, "openid": user_info["openid"], "session_key": user_info["session_key"]}
            redis_conn.set(jwt_key, str(val), settings.APP_EXP_SECOND)
            redis_conn.set('ccsf_xcx_user_' + user_info['openid'], jwt_key, settings.APP_EXP_SECOND)
            return (user, token)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()
        return (user, jwt_value)

    def bkd_check(self, jwt_key, user_info):
        jwt_value = user_info['token']
        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            user = AccountModel.objects.filter(id=user_info['user_id']).first()
            if not user:
                msg = _('用户不存在')
                raise exceptions.AuthenticationFailed(msg)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            val = {"token": token, "username": user.username, "user_id": user.id}
            redis_conn.set(jwt_key, str(val), settings.PC_EXP_SECOND)
            redis_conn.set('ccsf_bkd_user_' + str(user.id) + '_' + str(jwt_key, encoding='utf-8'), jwt_key, settings.PC_EXP_SECOND)
            return (user, token)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()
        try:
            user = self.authenticate_credentials(payload)
        except exceptions.AuthenticationFailed:
            msg = _('您的账户已被冻结')
            raise exceptions.AuthenticationFailed(msg)

        return (user, jwt_value)

    def my_jwt_payload_handler(self, payload):
        if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        if api_settings.JWT_AUDIENCE is not None:
            payload['aud'] = api_settings.JWT_AUDIENCE

        if api_settings.JWT_ISSUER is not None:
            payload['iss'] = api_settings.JWT_ISSUER
        return payload