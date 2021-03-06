#-*- coding:utf8 -*-

import JMQSTestLib
import json,base64

class TcRkmq():
    consume_queue_max = 32
    def __init__(self,iceconfig="ice.client",item="JMQSClient"):
        self.jmqsinst = JMQSTestLib.JMQSTest(iceconfig,item)
    def receive(self,rid,batchcount=10,maxWaitSeconds=1):
        failcount = 0
        all_result = []
        while failcount < TcRkmq.consume_queue_max:
            result = self.stoj(self.jmqsinst.pull_msg(rid, batchcount, maxWaitSeconds))
            if result[0][1] == 16:
                failcount += 1
            elif result[0][0] != -1:
                failcount = 0
                for x in result:
                    all_result.append(x[1])
            else:
                print('err code:',result[0][1])
        return all_result

    def send(self,rid,*msgs,**kw):
        all_msgs = JMQSTestLib.StringVector()
        type = 0
        if 'etype' in kw:
            type = int(kw['etype'])

        for msg in msgs:
            all_msgs.append(msg)

        p_result = self.stoj(self.jmqsinst.product_msg(rid, all_msgs,type))
        return p_result[0][1]

    def stoj(self,s):
        result = []
        j = json.loads(s)
        for i in j:
            data = i[1]
            if not isinstance(i[1], int):
                data = base64.b64decode(data)
            result.append((i[0], self.utou(data)))
        return result

    def utou(self,v):
        if isinstance(v, str):
            v = v.encode('utf8')
        return v

    def __del__(self):
        pass

if __name__ == "__main__":
    pass