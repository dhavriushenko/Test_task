# Test_task

### Project info

#### Tools

- Python 2.7.11
- Lettuce 0.2.21


#### BDD Feature files

[test/features](https://github.com/dhavriushenko/Test_task/edit/master/test/features)

### 
**To run  BDD test**

1. step by step:
  1. navigate to the project-root and install dependencies by: `pip install -r requirements.txt` or `sudo -H pip install -r requirements.txt` in case of Mac OSX
  2. install the project locally in development mode 
 ```pip install -e .``` (it creates a special .egg-link file in the deployment directory, that links to your project’s source code) or add path to your project folder in step.py (uncomment )
  2. start testing by:  ```lettuce  lettuce ''PATH_TO_PROJECT/Test_task/tests/features/Output.feature```
