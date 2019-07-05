# status-app

## CI pipeline

### Running locally

This application requires an installed and configured docker client connected to a Docker daemon.

The full CI pipeline is executed within a Docker container and the ```build.sh``` wrapper script can be run locally to test:

```
$ ./build.sh
```

The result will be a Docker image tagged with ```anz_test:<GIT COMMIT SHA>```


### From Cloud Build

At the root of this repository is a cloudbuild.yaml file. This can be used with [Google Cloud Build](https://cloud.google.com/cloud-build/) as a trigger target to build the Docker image and store it in Google Container Repository.

When run via the trigger, the image will be tagged with ```gcr.io/$PROJECT_ID/anz_test2:<GIT COMMIT SHA>``` and pushed to your projects GCR repository.

### High level CI steps

The CI pipeline performs the following steps:

* Installs 3rd party libraries
* Runs pylint to lint the code base and exits on linting errors
* Runs pytest to exercise unittests in ```tests``` sub directory and exits on any failures
* Runs safety to check if any 3rd part libraries have known security issues, exits if so.
* Second stage build to create a image with only runtime required libraries.

## Deployment

The container can be run as follows:

```bash
$ docker run -p5000:5000 anz_test2:latest
```


## Considerations

### Security - Supply chain

* The package dependencies are pinned. Only install known versions.

* A dependency scanner is used as part of the pipeline to determine if the dependencies have known vulnerabilities. Abort pipeline if vulnerabilities detected.

### Quality - Code coverage - pytest

 * pytest coverage 100%. Abort the pipeline if it is lower.

### Quality - Code style - pylint

 * The official Python style is comprehensive and covered in a Python standard document [PEP-8](https://www.python.org/dev/peps/pep-0008/). `pylint` is the tool that enforces this standard. Abort the pipeline if pylint returns non-zero

### Versioning - Traceability 

* Versioning is handled by tagging the image in the current commit SHA1 hash as well as baking it in as an environment variable which the application returns on the `/status` end point. There is also a static VERSION.txt that can be incremented by release processes outside of CI (although may be attached to tagging in the future) to allow a more human readable versioning. Tagging with the hash allows for builds on any branch without risk of duplication and zero coupling to build infrastructure by avoiding build numbers. 

## Limitations and Risks

* Container image currently uses the built in flask web server. This is not production grade and should be swapped out before being deployed into a live environment.
* The application code is a simple example only. It does not implement any error handling and will crash if environment variables are not set correctly as an example.
* Outside of a dependency scanner there is no security scanning performed in the CI pipeline. Options around static / dynamic code scanning should be considered.
* The base python image used is quite large. Look at options to reduce this. Potentially using Alpine Linux as a base for example.
* Dependencies are pinned but still pulled from the internet. In a secure environment would suggest using only private repository of 3rd party libraries that have already been scanned to help ensure a secure software supply chain.
* No set branching strategy is enforced. The CI pipeline is designed with the ability to run on short lived branches for testing, producing images independent of any trunk based images.
* No monitoring or metrics have been defined for the application. SLOs/SLIs would need to be defined so that the application could be uplifted to acceptable level and ensure we have the required level of observability.
* A full continuous delivery (CD) pipeline should be created when deploying to production. 