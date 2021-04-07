import sys
import base64
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators

@Configuration()
class CyberCommands(StreamingCommand):

    field = Option(
        doc='''
        **Syntax:** **field=***<fieldname>*
        **Description:** Name of the field which contains the value''',
        require=False, validate=validators.Fieldname())

    def stream(self, records):
        # check if the field value was specified
        if self.field == None:
            raise Exception("The field must be specified!")
        else:
            for record in records:
                # get value from field
                payload = record[self.field]
                # encode payload
                payload_enc = payload.encode('utf-8').hex()
                # creating a new var using suffix _enc
                record[self.field+"_enc"] = payload_enc
                yield record

if __name__ == "__main__":
    dispatch(CyberCommands, sys.argv, sys.stdin, sys.stdout, __name__)
