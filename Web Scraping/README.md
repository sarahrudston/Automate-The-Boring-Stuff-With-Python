<h2>Practice Questions</h2>

1. Briefly describe the differences between the `webbrowser`, `requests` and `bs4` modules.<br>
*The `webbrowser` module can only open URLs. The `requests` module allows downloading of files from the web. `bs4` (Beautiful Soup) is a package for extracting information from an HTML page.*

2. What type of object is returned by `requests.get()`? How can you access the downloaded content as a string value?<br>
*`requests.get()` returns a `Response` object. To access as a string value, you can store the result in a variable and call `.text` on it.*

3. What `requests` method checks that the download worked?<br>
*You can check that the request for a web page succeeded by checking that the `Response` object's `status_code` attribute is equal to `requests.codes.ok`. You can also call `raise_for_status()` which will raise an exception if an error occurred while downloading the file.*

4. How can you get the HTTP status code of a requests response?<br>
*You can store the request in a variable and then use `response.status_code` to see the status code of a requests response.*

5. How do you save a requests response to a file?<br>
*You can use the standard `open()` function and `write()` method to save a web page to a file, however you have to open the file in write binary mode by passing `wb` to `open()`.*

6. What two formats do most online APIs return their responses in?<br>
*Most APIs return their responses in either XML or JSON format.*

7. What is the keyboard shortcut for opening a browser's Developer Tools?<br>
*In Firefox, Chrome and Edge, you can press F12 to make the Developer Tools appear.*

8. How can you view (in the Developer Tools) the HTML of a specific element on a web page?<br>
*You can right-click any part of the web page and select Inspect Element from the context menu to bring up the HTML responsible for that page in the Developer Tools.*

9. What CSS selector string would find the element with an id attribute of `main`?<br>
*You can retrieve a web page element from a BeautifulSoup object by calling `select()` and passing a selector string for the element you're looking for. For example `soup.select('#main')`.*

10. What CSS selector string would find the elements with an id attribute of highlight?<br>
*`soup.select('highlight')`*

11. Say you have a Beautiful Soup Tag object stored in the variable `spam` for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?<br>
*You can pass the variable to the str() function to show the contents as a string. For example, `str(spam)`. If you want to then show the actual text, you can use `spam.get_text()` which will return 'Hello, world!'*

12. How would you store all the attributes of a Beautiful Soup Tag object in a variable named `link_elem`?<br>
*The `attrs` attribute contains all the variables attributes as a dictionary. Therefore you should pass `link_elem.attrs` to a variable.*

13. Running `import selenium` doesn't work. How do you properly import Selenium?<br>
*You have to run `selenium import webdriver`.*

14. What's the difference between the find_element() and find_elements() methods in Selenium?<br>
*`find_element()` finds a single `WebElement` object, which is the first element on the page that matches the query. `find_elements()` returns a list of `WebElement` objects for every matching element. *

15. What methods do Selenium's WebElement objects have for simulating mouse clicks and keyboard keys?<br>
*The `click()` method simulates a mouse click on that element. The `send_keys()` method allows the user to send keystrokes to text fields on the page.*

16. In Playwright, what locator method call simulates pressing CTRL-A to select all the text on the page?<br>
*Key presses can be simulated in Playwright using the `press()` method on Locator objects. You can pass 'Control+A' for CTRL-A to select all text on the page.*

17. How can you simulate clicking a browser's Forward, Back, and Refresh buttons with Selenium?<br>
*Selenium can simulate clicks on various browser buttons through `browser.back()`, `browser.forward()` and `browser.refresh()`.*

18. How can you simulate clicking a browser's Forward, Back, and Refresh buttons with Playwright?<br>
*Playwright can simulate clicking the browser buttons by calling the following `Page` methods on the `Page` object returned by `browser.new_page()`: `page.go_back()`, `page.go_forward()`, `page.reload()`.*




