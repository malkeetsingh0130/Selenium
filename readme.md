1. whenver we start the code we have to import slenium webdriver
2. we need to specify the path for the webdriver that we will use using service object
    a. for this we will need to import service
3. driver.get is used to open the website that we want
4. driver.maximize_window will make the session full screen
5. driver.find_element(By.) is used to identify elements
    a. we have below methods for identifying elements
        1. ID
        2. NAME
        3. LINK Text/ PARTIAL LINK TEXT - this is used in case of links where id or name is not available
        4. classname and tag name are used when we want to find more than one element. we need to use driver.findelements() if we want to find more than 1 element or else it will just list the first.
            a. for example you want to find total number of sliders in a page. 
            b. for links we will always have tag "a".
        5. CSS selectors- these are not directly listed in html
            tag is always optional
            a. tag and id -syntax: tag_name#id
            b. tag and class- syntax: tag_name.value_class 
                Sometimes it doesnt take the value of class if there is whitespace in it. we can remove the items after the space to make it work
                    ex. "input_error form_input" here we can remove from_input to make it work
            c. tag and attribute
            d. tag,class and attribute

