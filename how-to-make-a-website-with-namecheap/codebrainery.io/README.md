# Codebrainery.io

Codebrainery.io is a learn-to-code website. Let’s build their homepage using a combination of Bootstrap and custom CSS, provided by the file style.css.

## Tasks

1. Start by linking to Bootstrap. In index.html, inside the head element, create a link element with an href attribute that points to:

```bash
https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css
```

2. Next create the `header` with `navbar` in `index.html`.

Steps:

  a. Start with a header element with class “container”.
  b. Inside the header, add a div with the class “row”.
  c. Inside the div, create:
    - an h1 element with the class “col-sm-8”. Have it display the text “Codebrainery.io”.
    - `nav` element with a class of `“col-sm-4”`.
  d. Inside the `nav`, create three `p` elements to list navbar items: `“Sign In”`, `“Sign Up”` and `“About”`.

3. Now, let’s enhance the `navbar` with some custom CSS.

  a. In `index.html`, locate the `p` elements which display the navbar choices “Sign In” and “Sign Up”.
  b. Give the `p` that displays “Sign In” a class of `“pill-white”`.
  c. Give the `p` that displays “Sign Up” a class of `“pill-black”`.

The `“pill-white”` and `“pill-black”` classes are located in `style.css`. If you are curious, open the file and take a look at how those rules are implemented.

4. Now create a jumbotron section to display Codebrainery.io’s new course: Build a Website.

Steps:

  a. In `index.html`, below the `</header>` tag, create a `section` element with the `“jumbotron”` class.
  b. Inside the `section`, add a `div` with the class `“container”`.
  c. Inside the `div`, add another `div` with the class `“row text-center”`.
  . Inside the `div` with class `“row text-center”`, add an `h2` element that displays the text `“New Course Release”`.
  e. Below the `h2`, add an `h3` element that displays the text `“Build a Website”`.

5. Next, add a supporting content section to display the courses taught on codebrainery.io.

Steps:

  . In `index.html`, below the closing `</section>` tag, create another section element with a class of “container”.
  b. Inside the section, add two `div` elements, and give each a class of `“row”`.
  c. Inside each `“row”` `div`, create three `figure` elements, each with a class of `“col-sm-4”`.
  d. Inside each `figure`, add an image element containing one of the following image URLs:

Ruby

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/ruby.png
```

JavaScript

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/javascript.png
```

MySQL

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/mysql.png
```

PHP

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/php.png
```

jQuery

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/jquery.png
```

Python

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/python.png
```

6. Below the supporting content section add a link for the site visitor to view all courses codebrainery.io has to offer.

Steps:

a. To start, add a `div` with the class `“row text-center”`.
b. Inside the `div`, add an anchor element with the class `“btn btn-primary”`.
c. Give the anchor element an `href` attribute and set its value to `“#”`, as a placeholder for a URL.
d. Have the anchor element display the text `“View All Courses”`.

7. Now add a footer to the bottom of the webpage. The footer will display the name of the website and links to social media sites.

Steps:

a. Start by creating a footer element with the class `“container”`.
b. Inside the `footer`, create a `div` with the class `“row”`.
c. Inside the `div`, create a `p` element and a `ul` element.
d. Give the `p` element a class of `“col-sm-4”`.
e. Have the `p` element display the text “codebrainery.io”.
f. Give the `ul` a class of `“col-sm-8 text-right”`.
g. Add four list items inside the `ul`.
h. Give each list item a class of `“col-sm-1”`.
i. Inside each list item, add an image element.
j. Assign the image `src` attributes to these image URLs:

Facebook

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/facebook-grey.svg
```

Twitter

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/twitter-grey.svg
```

Instagram

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/instagram-grey.svg
```

Medium

```html
https://content.codecademy.com/projects/make-a-website/lesson-4/medium-grey.svg
```

For help, [here](https://codecademy.com/couses/make-a-website/lessons/bootstrap/exercises/footers) is the exercise that introduced using Bootstrap to create a footer.
