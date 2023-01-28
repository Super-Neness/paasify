# Installation

There are several way of installing paasify, but the recommended way is the pip way. If you want to develop or
patch paasify, you will want to [install paasify with git](install) instead.




## Install with Pip

To install pip in your home:

```
pip install --user paasify
```

## Install with Docker

!!! warning "About using this install method"

    Using docker install method is the quickest to test paasify, however this
    method is limited and will not work if you reference files outside of your
    project directory. This install method is more to for quick try or production
    deployment.


Basically, you can run the docker image this way:

```
docker run --rm -v $PWD:/work -ti ghcr.io/barbu-it/paasify:latest --help
```

You can make a more convenient shell wrapper:
```
$ sudo cat <<EOF > /usr/local/bin/paasify
#!/bin/bash

docker run --rm -v $PWD:/work -ti ghcr.io/barbu-it/paasify:latest $@
EOF
$ sudo chmod +x /usr/local/bin/paasify
```
