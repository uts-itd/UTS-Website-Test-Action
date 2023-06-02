# uts-chinese-website-ui-test
<div align="center">
  <img height="400" src="https://i.imgur.com/s0CDqF5.png" />

   <br>
  <small> <b><i>Show your support!</i> </b></small>
  <br>
   <a href="https://github.com/MarketingPipeline/Python-Selenium-Action">
    <img title="Star on GitHub" src="https://img.shields.io/github/stars/MarketingPipeline/Python-Selenium-Action.svg?style=social&label=Star">
  </a>
  <a href="https://github.com/MarketingPipeline/Python-Selenium-Action/fork">
    <img title="Fork on GitHub" src="https://img.shields.io/github/forks/MarketingPipeline/Python-Selenium-Action.svg?style=social&label=Fork">
  </a>
   </p>  
 
 


   
 
No need to struggle to figure out how to run a Python Selenium script with a  [GitHub Action](https://github.com/features/actions). 
  This is a <b>ready to use</b> template for running Selenium with Python via [GitHub Actions](https://github.com/features/actions) on non-headless. <br> 
</div>



## Example and usage


To use <b><i>Github Action</b></i>:

- Push/merge any code to the main branch and it will run the tests on the UTS website on Github Actions

- Make changes as needed to the Python script <code>utilities.py</code>. 

- Make changes as needed to the <code>Selenium-Action.yaml</code> file. For Github actions.

## Runthrough Breakdown
1. It will first click on each button on the side bar and then go back to the home page each time it's clicked
2. Then it will go to the search icon at the top-right of the page to search for 'careers'
3. Then it will click on the first result that comes up
4. It will go back to the home page and test the slick arrows right below "LX at UTS"
5. Then it will click on the article that is present at the time
6. Steps 4 and 5 will be repeated 2 more times. 
<br>

## Demo(s) 
An example of the script sucessfully running on GitHub:
- [Successful Action Run](https://github.com/uts-itd/UTS-Website-Test-Action/actions/runs/5150555527)


## Branches:
- main, selenium-grid: Run tests on Selenium Grid
  
## Contributing

Want to improve this? Create a pull request with detailed changes / improvements! If approved you will be added to the list of contributors of this awesome project!



See also the list of
[contributors](https://github.com/uts-itd/UTS-Website-Test-Actions/graphs/contributors) who
participate in this project.


