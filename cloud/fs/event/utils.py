from cloud.fs.event import base
from cloud.fs.settings import fs_settings
from cloud.fs.utils import encrypt_mobile


class Utils(base.BaseEvent):
    def originate_queue_test(self,
                             mobile,
                             queue_name,
                             caller='',
                             phoneId='',
                             gateway=None):
        '''呼叫
        mobile: 坐席回显的号码
        queue_name: 外呼队列
        caller: 送达vos主叫
        phoneId: 呼叫号码id
        gateway: 外呼使用网关
        '''
        if not gateway:
            gateway = fs_settings.DEFAULT_GATEWAY_NAME
        msg = """originate {{sip_h_X-Phoneid={phoneId},cc_export_vars=sip_h_X-Phoneid,origination_caller_id_number={caller},effective_caller_id_number={encrypt},call_timeout=30,agent_timeout=5,originate_timeout=30}}sofia/gateway/{gateway}/{mobile} {queue_name}""".format( # noqa
            **{
                'phoneId': phoneId,
                'caller': caller,
                'mobile': mobile,
                'encrypt': encrypt_mobile(mobile),
                'gateway': gateway,
                'queue_name': queue_name
            })
        return self.send(msg)
