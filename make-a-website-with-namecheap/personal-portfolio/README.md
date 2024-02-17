Skip to Content
Project
Code
Output

Building a Personal Portfolio
Project Brief
Objective
HOW TO MAKE A WEBSITE WITH NAMECHEAP
Building a Personal Portfolio
Building a personal portfolio provides an immediate demonstration of your programming prowess for prospective employers. It’s important, therefore, that this webpage appears clean and well-organized. A user should easily understand a particular page’s content and navigate seamlessly through your different pages.

You will be making several different webpages so it’s perfectly ok, and even recommended, to take breaks after completing each page. Also keep in mind that we’re providing not only guidelines on a very specific design but also the CSS which has established fonts, spacing, etc. that work for this particular design. Feel free to add, remove, or modify any details on a given page.

Tasks
1/33 complete
Mark the tasks as complete by checking them off
The Home Page
1.
Let’s start your personal portfolio by building the home page - the initial landing page for anyone who visits your website. Click here to see what your home page should look like by the end of this task.

2.
Making the Header

Let’s begin crafting your navigation header, which will offer a user other pages to visit. Within the body, create a header element with Bootstrap’s container class. When you run your code, it will appear as if nothing has changed. That’s perfectly alright because you’re setting up the containers where the text will appear.


Hint
Give the header the correct class.

<body>
    <header class="_________">
    </header>
</body>

3.
Within this opening container, create a div with the Bootstrap class row.


Hint
Give the div the correct class.

<header class="container">
    <div class="_________">
    </div>
</header>

4.
Within this row, create an h1 with Bootstrap’s class col-sm-6 and put your name between the opening and closing h1 tags. Save your code and observe that now you have visible content.


Hint
Give the h1 the correct class.

<div class="row">
    <h1 class="_________">Your Name</h1>
</div>

5.
Underneath the h1, add a nav element with Bootstrap’s class col-sm-6 text-right.


Hint
Give the nav element the correct class.

<div class="row">
    <h1 class="col-sm-6">Your Name</h1>
    <nav class="_________">
    </nav>
</div>

6.
This nav element will have three a elements with href properties. Create three links:

about.html linked to the text “About Me”
education.html linked to the text “Education”
experience.html linked to the text “Experience”
You will build these HTML files later in the project. Resize the browser component by clicking on the double-arrow to the right of http://localhost:8000/ to observe how it adjusts to different size screens.


Hint
Remember to add the correct path to the appropriate a element.

<div class="row">
    ...
    <nav class="col-sm-6 text-right">
        <a href="_________">About Me</a>
        <a href="_________">Education</a>
        <a href="_________">Experience</a>
    </nav>
</div>

7.
Making the Jumbotron

The next section you’ll build is the jumbotron, which will showcase to the user what the page offers. Below our header element, create a section element with the jumbotron class. We’ve set a default background image in the CSS file to that of a skyline. You’re welcome (and encouraged) to choose your own image for free at unsplash.com.


Hint
Remember that you’re not in the header anymore.

<body>
    <header>
    ...
    </header>
    <section class="_________">
    </section>
    ...
</body>

8.
Within this jumbotron, make a container with a single row, similar to steps 1 & 2 when making the header. This time, the container will be a div, not a header.


Hint
Remember that you’re not in the header anymore.

<div class="_________">
    <div class="_________">
    </div>
</div>

9.
Inside this row, create an h2 that states your position as a programmer.


Hint
The h2 is nested inside of the row.

<div class="row">
    <h2>_________</h2>
</div>

10.
Underneath the h2, add an h3 that lists the programming languages you know.


Hint
The h3 is a sibling of the h2.

<div class="row">
    <h2>_________</h2>
    <h3>_________</h3>
</div>

11.
Making the Footer

Finally, let’s complete our home page with a footer element which will offer outside resources for prospective employers to explore. Below the jumbotron element, create a footer element with the container class with a single row nested inside of it.


Hint
Remember that you’re not in the jumbotron anymore.

<footer class="_________">
    <div class="_________">
    </div>
</footer>

12.
Within this row, add a paragraph with Bootstrap’s col-sm-4 class that lists &copy; 2019 Your-Name.


Hint
Give the p element the correct class.

<div class="row">
    <p class="_________">_________</p>
</div>

13.
Under this paragraph, add four divs, each with the class col-sm-2.


Hint
The four divs are siblings of the paragraph.

<p class="col-sm-4">_________</p>
<div class="_________">
</div>
<div class="_________">
</div>
…

14.
Each div will have an a element with an href property. Create four links for the hrefs:

“Medium” - https://medium.com/
“Github” - https://github.com/
“LinkedIn” - https://www.linkedin.com/
“Podcast” - https://tunein.com/podcasts/
Each anchor element should open the website it references in a separate window. NOTE - these URL’s are just some suggestions, particularly if you have profiles with these websites. Feel free to link up to other websites of your choice.


Hint
Add target="_blank" so that the a href will open a new window.

<div class="col-sm-2">
    <a href="_________" target="_________">Medium</a>
</div>
<div class="col-sm-2">
    <a href="_________" target="_________">Github</a>
</div>
...

The About Me Page
15.
Great work! You have your home page set up, let’s focus now on the “About Me” page, which will offer a brief summary of who you are as a person. Click on the “About Me” link in your header to navigate to this new page.

If you’d like, click here to see what your “About Me” page should look like by the end of this task.

16.
Making the Header

Just like the home page, you will first have to create another navigation header. Luckily, the header element (and all of its nested elements) will be nearly identical to the one you already created in the home page! Copy the entire header element from the index.html page and paste it within the top of the body element within your about.html page. The only change will be switching the first href value from about.html to index.html and replacing the corresponding text with “Home”.


Hint
Make sure the header element goes inside the body element.

<body>
    <header>
    …
    </header>
</body>

17.
Making the Jumbotron

Similar to the home page, you’ll need a section element with the jumbotron class. Copy the entire jumbotron section from your home.html page and paste it into your about.html page underneath the header element. Inside of this newly duplicated row, delete the existing h3 element and modify the h2 element so that it now says “About Me” instead of your original role of developer.


Hint
Remember to delete the h3 and modify the h2.

<section class="jumbotron">
    <div class="container">
        <div class="row">
            <h2>_________</h2>
        </div>
    </div>
</section>

18.
Making the Content

Now we’ve reached the part of the site that will present who you are as a person. Underneath the jumbotron section, create a section container with a div with the classes row and justify-content-center.


Hint
An element can have more than one class by separating the classes with a space.

<section class="________">
    <div class="class-1 class-2">
    </div>
</section>

19.
Inside of this row, add another div with a col-sm-6 class.


Hint
Give the div element the correct class.

<div class="row justify-content-center">
    <div class="_________">
    </div>
</div>

20.
Nested inside of this div will be an img element with an src which is a url that is a picture of you.


Hint
Use a url as the value of the src like https://content.codecademy.com/projects/personal_portfolio/profile_image.jpg, for example.

<img src="_________">

21.
Underneath this img element add a paragraph that describes who you are and what you’re passionate about. This paragraph should be 4-5 sentences in length.


Hint
The p element is a sibling of the img element.

<img src="_________">
<p></p>

22.
Making the Footer

Fortunately, the footer element (and all of its nested elements) are identical to the one you created in the home page. Copy the entire footer element from the home.html page and paste it at the bottom of the about.html body element.


Hint
Make sure the footer element is at the bottom of the body element.

    <footer>
    ...
    </footer>
</body>

The Education Page
23.
Excellent - you now have two functioning pages on your portfolio! Next, let’s build an Education page which will allow employers to see your traditional (or non-traditional) educational background. Click on the “Education” link in your header to navigate to this new page.

If you’d like, click here to see what your “Education” page should look like by the end of this task.

24.
Making the Header, Jumbotron, and Footer

Copy the entire header, jumbotron, and footer elements from the about.html page and paste it into the body element of your education.html page. In the header, switch the second href value from education.html to about.html and replace the corresponding text with “About Me”. In the jumbotron, relabel the h2 from “About Me” to “Education”.


Hint
Remember to modify the h2 of the jumbotron.

<section class="jumbotron">
    <div class="container">
        <div class="row">
            <h2>_________</h2>
        </div>
    </div>
</section>

25.
Making the Content

Now, let’s make a section that has one row and two columns. Under the jumbotron element, add a section tag with the class container with a single row. Within this row, add two divs — each with the class col-sm-6.


Hint
Give the section and div elements the correct class.

<section class="_________">
    <div class="_________">
        <div class="_________">
        </div>
        <div class="_________">
        </div>
    </div>
</div>

26.
Within the first column you just created, add a paragraph element to show the name of your high school, an image of your high school’s logo, and an unordered list with several accomplishments. The paragraph has a font-weight-bold class and the image has a class of portrait.


Hint
All these elements within the div are siblings.

<div class ="col-sm-6">
    <p class="_________">_________</p>
    <img class="_________" src="_________">
    <ul>
        <li>_________</li>
        …
    </ul>
</div>

27.
Within the second column you just created, add a paragraph element to show the name of your university, an image of your university’s logo, and an unordered list with several accomplishments. The paragraph has a font-weight-bold class and the image has a class of portrait.


Hint
All these elements within the div are siblings.

<div class ="col-sm-6">
    <p class="_________">_________</p>
    <img class="_________" src="_________">
    <ul>
        <li>_________</li>
        …
    </ul>
</div>

The Experience Page
28.
You’re almost done with your personal portfolio! Let’s move onto building the final page of your personal portfolio - the Experience page. This page will outline any and all relevant experiences you’ve had with programming languages or the tech industry. Whether that experience is in the form of professional or personal projects, it’s always a good idea to update this page constantly to let prospective employers know you’re staying active and proactive in honing your craft as a developer! Click on the “Experience” link in your header to navigate to this new page.

If you’d like, click here to see what your “Experience” page should look like by the end of this task.

29.
Making the Header, Jumbotron, and Footer

Copy the entire header, jumbotron, and footer elements from the about.html page and paste it into the body element of your education.html page. In the header, switch the third href value from experience.html to education.html and replace the corresponding text with “Education”. In the jumbotron, relabel the h2 from “Education” to “Experience”.


Hint
Remember to modify the h2 of the jumbotron`.

<section class="jumbotron">
    <div class="container">
        <div class="row">
            <h2>_________</h2>
        </div>
    </div>
</section>

30.
Making the Content

Next, let’s create a visual representation of your programming language experience. Under the jumbotron element, create a section container with one row and four columns (using col-sm-3) within that row. Each column contains an h5 for the name of the programming language, an img of the language’s logo, and an unordered list with a single li element stating how long you’ve worked with that particular language.


Hint
Remember to correctly nest your elements and give them the correct class.

<section class="container">
    <div class="row">
        <div="col-sm-3">
            <h5>Java</h5>
            <img src="https://content.codecademy.com/projects/personal_portfolio/java.jpg">
            <ul>
                <li>4 years experience</li>
            </ul>
        </div>
        ...
    </div>
</section>

31.
Finally, let’s create one last section container underneath the programming language section which will list your professional and personal projects. Inside this section will be an h2 that states “Professional Projects” and one row. This row will have an unordered list element where each li element will be a professional project where you applied your programming skills or participated in the tech industry.


Hint
Remember to correctly nest your elements and give them the correct class.

<section class="_________">
    <h2>_________</h2>
    <div class="_________">
        <ul>
            <li>_________</li>
            ...
        </ul>
    </div>
</section>

32.
Underneath this row, create another h2 that states “Personal Projects” and one row. This row will have an unordered list element where each li element will be a personal project where you applied your programming skills or volunteered in the tech industry.


Hint
Remember to correctly nest your elements and give them the correct class.

<section class="_________">
    ...
    <h2>_________</h2>
    <div class="_________">
        <ul>
            <li>_________</li>
            ...
        </ul>
    </div>
</section>

Next Steps
33.
Congratulations! You’ve created a fully functioning personal portfolio with four HTML pages that link up with CSS and Bootstrap! If you’re looking to expand on your personal portfolio, try creating a “Contact Me” page with your personal information so prospective employers can reach out to you directly. One “Contact Me” page idea would look like this. Make sure to update your header for any new pages that you add. Also, see if you can add a button at the bottom of each page (but above the footer) that will return a user to the home page. Next, let’s learn how to deploy your personal portfolio to the Internet!


