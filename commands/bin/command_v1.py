# -*- coding: utf-8 -*-
import sys
import splunk.Intersplunk

payload = "payload"

results = []
try:
        #Busca os resultados da pesquisa no Splunk
        results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()

        for r in results:
                if payload in r:
                        try:
                                each_payload = r[payload]
                                # DO SOMETHING HERE WITH EACH STRING
                        except:
                                r["out"] = "Error!"

except:
        import traceback
        stack =  traceback.format_exc()
        results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))

#Retorna os resultados para a search no Splunk
splunk.Intersplunk.outputResults(results)
