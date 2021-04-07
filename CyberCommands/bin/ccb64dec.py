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
                # decode payload
                payload_dec = base64.b64decode(payload)
                # creating a new var using suffix _dec
                record[self.field+"_dec"] = payload_dec.decode('utf-8')
                yield record

if __name__ == "__main__":
    dispatch(CyberCommands, sys.argv, sys.stdin, sys.stdout, __name__)
