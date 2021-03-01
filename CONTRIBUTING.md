# Contributing to this library are Welcome

This is a guide for you to get some ideas~

## Dependencies
To make sure that the following instructions work, you will need to have the dependencies installed. To install them all at once, you can use pipenv: `pipenv install` after cloning the repository.

Alternatively, you can manually install the following dependencies:
- requests,
- unidecode,
- nltk,
- docx2txt,
- PyPDF2,
and for testing:
- coveralls==1.1
- pytest

## Installation

To get the source of `py-googletranslation`, clone the git repository via:

````
$ git clone https://github.com/Saravananslb/py-googletranslation
````
This will clone the complete source to your local machine.

## Issue Reporting

Feel free to report any issues that you come up with!
Please follow the steps before reporting. We love keeping everything in a good manner :p

### Step 1: Checking Previous Issues

There may be a lot of different issues related to different aspects.  
Here we list 12 main types:  

* [bug](https://github.com/Saravananslb/py-googletranslation/labels/bug)
* [compromised](https://github.com/Saravananslb/py-googletranslation/labels/compromised)
* [dependencies](https://github.com/Saravananslb/py-googletranslation/labels/dependencies)
* [duplicate](https://github.com/Saravananslb/py-googletranslation/labels/duplicate)
* [enhancement](https://github.com/Saravananslb/py-googletranslation/labels/enhancement)
* [help wanted](https://github.com/Saravananslb/py-googletranslation/labels/help%20wanted)
* [in progress](https://github.com/Saravananslb/py-googletranslation/labels/help%20wanted)
* [invalid](https://github.com/Saravananslb/py-googletranslation/labels/invalid)  

Please see [About labels](https://docs.github.com/en/github/managing-your-work-on-github/about-labels) for more information.  

Note there is no labels for closed issues but still remember to have a look!  

### Step 2: Formatting Your Comment

Please see the [Issue Template](ISSUE_TEMPLATE.md).

## Pull Request Submitting

> Inspired by https://github.com/ssut/py-googletrans/CONTRIBUTING.md.  
- Check out a new branch based on <code>master</code> and name it to what you intend to do:
  - Example:
    ````
    $ git checkout -b BRANCH_NAME origin/master
    ````
    If you get an error, you may need to fetch master first by using
    ````
    $ git remote update && git fetch
    ````
  - Use one branch per fix/feature
- Make your changes
  - Make sure to provide a spec for unit tests.
  - Run the tests ``pytest``.
  - Add a test for your feature or bug fix.
  - When all tests pass, everything's fine. If your changes are not 100% covered, go back and 
    run the tests ``pytest`` again
- Commit your changes
  - Please provide a git message that explains what you've done.
  - Please make sure your commits follow the [conventions](https://www.conventionalcommits.org/en/v1.0.0/)
  - Commit to the forked repository.
- Make a pull request
  - Make sure you send the PR to the <code>master</code> branch.
  - Link the bug issue if there is one.
  - Travis CI is watching you!

If you follow these instructions, your PR will land pretty safely in the main repo!  
  
