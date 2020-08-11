import sys
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration

@Configuration()
class SampleCommand(StreamingCommand):
    def stream(self, records):
        for record in records:
            each_payload = record['payload']
            # DO SOMETHING HERE WITH EACH STRING
            yield record

if __name__ == "__main__":
    dispatch(SampleCommand, sys.argv, sys.stdin, sys.stdout, __name__)
