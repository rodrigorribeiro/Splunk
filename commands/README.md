# commands - Sample App
> This app should be used as a sample to create new apps with the purpose of extending SPL with custom commands.

This code in python can receive Splunk stdin do something into python code and return stdout to Splunk.

Basicaly: SPL -> Python Code -> SPL

## Requirements

There are not requirements:

## Installation

You need to put this folder into: $SPLUNK_HOME/etc/apps/

## Usage example

You need to specify only on argument, example:

```sh
index=<name> | eval payload = _raw | command | table out
```

All variables can be changed, both in input and output.

Attention, see the code in python command.py there will be a comment in the code of the exact location where your customized operations should be executed.

## Release History

* 1.0.0
    * The first proper release

## Meta

Rodrigo Ribeiro – [@silvarribeiros](https://twitter.com/silvarribeiros) – silva.rrs@gmail.com

[https://github.com/rodrigorribeiro/](https://github.com/rodrigorribeiro/)

## Contributing

1. Fork it (<https://github.com/rodrigorribeiro/Splunk/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
