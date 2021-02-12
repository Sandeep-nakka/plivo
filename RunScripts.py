import requests
import json
import subprocess


class testscenerios:
    # / opt / sipp - 3.3 / sipp - sf / home / xpms / Desktop / sipp_uac_register2.xml - i 192.168.1.101 - p 5064phone.plivo.com - m 1 - aa - trace_screen - trace_msg - trace_err

    def sipp_start(self):
        sipp_uac='/sipp_uac'
        sipp_register='/sipp_uac_register1.xml'
        sipp_uas='/sipp_uas'
        sipp_register2='/sipp_uac_register2.xml'

        output1=subprocess.Popen('%s %s' % (sipp_uac, sipp_register), shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output1)
        output2=subprocess.Popen('%s %s' % (sipp_uas, sipp_register2), shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output2)

        sipp_uac1='sipp_uac1'
        sipp_uac1_xml='sipp_uac1.xml'
        sipp_uas1='sipp_uas1'
        sipp_uas_xml='sipp_uas1.xml'
        output3 = subprocess.Popen('%s %s' % (sipp_uac1, sipp_uac1_xml), shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output3)
        output4 = subprocess.Popen('%s %s' % (sipp_uas1, sipp_uas_xml), shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output4)


run = testscenerios()
run.sipp_start()
