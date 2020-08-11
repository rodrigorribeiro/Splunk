import sys
import base64
import zlib
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration

@Configuration()
class SampleCommand(StreamingCommand):
    def stream(self, records):
        for record in records:
            each_payload = record['payload']
            b64 = base64.b64decode(each_payload)
            record["out"] = zlib.decompress(b64).decode('utf-8')
            yield record

if __name__ == "__main__":
    dispatch(SampleCommand, sys.argv, sys.stdin, sys.stdout, __name__)
