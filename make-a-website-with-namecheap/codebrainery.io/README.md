Skip to Content
My Home
Syllabus

Fork
Get Unstuck
Tools

Avatar
Codebrainery.io
Project Brief
Objective
HOW TO MAKE A WEBSITE WITH NAMECHEAP
Codebrainery.io
Codebrainery.io is a learn-to-code website. Let’s build their homepage using a combination of Bootstrap and custom CSS, provided by the file style.css.

If you get stuck during this project, check out the project walkthrough video which can be found in the help menu.

Tasks
5/7 complete
Mark the tasks as complete by checking them off
Codebrainery.io
1.
Start by linking to Bootstrap. In index.html, inside the head element, create a link element with an href attribute that points to:

https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css


Stuck? Get a hint
2.
Next create the header with navbar in index.html.

Steps:

a. Start with a header element with class “container”.

b. Inside the header, add a div with the class “row”.

c. Inside the div, create:

an h1 element with the class “col-sm-8”. Have it display the text “Codebrainery.io”.
a nav element with a class of “col-sm-4”.
d. Inside the nav, create three p elements to list navbar items: “Sign In”, “Sign Up” and “About”.


Stuck? Get a hint
3.
Now, let’s enhance the navbar with some custom CSS.

a. In index.html, locate the p elements which display the navbar choices “Sign In” and “Sign Up”.

b. Give the p that displays “Sign In” a class of “pill-white”.

c. Give the p that displays “Sign Up” a class of “pill-black”.

The “pill-white” and “pill-black” classes are located in style.css. If you are curious, open the file and take a look at how those rules are implemented.


Stuck? Get a hint
4.
Now create a jumbotron section to display Codebrainery.io’s new course: Build a Website.

Steps:

a. In index.html, below the </header> tag, create a section element with the “jumbotron” class.

b. Inside the section, add a div with the class “container”.

c. Inside the div, add another div with the class “row text-center”.

d. Inside the div with class “row text-center”, add an h2 element that displays the text “New Course Release”.

e. Below the h2, add an h3 element that displays the text “Build a Website”.


Stuck? Get a hint
5.
Next, add a supporting content section to display the courses taught on codebrainery.io.

Steps:

a. In index.html, below the closing </section> tag, create another section element with a class of “container”.

b. Inside the section, add two div elements, and give each a class of “row”.

c. Inside each “row” div, create three figure elements, each with a class of “col-sm-4”.

d. Inside each figure, add an image element containing one of the following image URLs:


Ruby:

https://content.codecademy.com/projects/make-a-website/lesson-4/ruby.png

JavaScript:

https://content.codecademy.com/projects/make-a-website/lesson-4/javascript.png

MySQL:

https://content.codecademy.com/projects/make-a-website/lesson-4/mysql.png

PHP

https://content.codecademy.com/projects/make-a-website/lesson-4/php.png

jQuery

https://content.codecademy.com/projects/make-a-website/lesson-4/jquery.png

Python

https://content.codecademy.com/projects/make-a-website/lesson-4/python.png


Stuck? Get a hint
6.
Below the supporting content section add a link for the site visitor to view all courses codebrainery.io has to offer.

Steps:

a. To start, add a div with the class “row text-center”.

b. Inside the div, add an anchor element with the class “btn btn-primary”.

c. Give the anchor element an href attribute and set its value to “#”, as a placeholder for a URL.

d. Have the anchor element display the text “View All Courses”.


Stuck? Get a hint
7.
Now add a footer to the bottom of the webpage. The footer will display the name of the website and links to social media sites.

Steps:

a. Start by creating a footer element with the class “container”.

b. Inside the footer, create a div with the class “row”.

c. Inside the div, create a p element and a ul element.

d. Give the p element a class of “col-sm-4”.

e. Have the p element display the text “codebrainery.io”.

f. Give the ul a class of “col-sm-8 text-right”.

g. Add four list items inside the ul.

h. Give each list item a class of “col-sm-1”.

i. Inside each list item, add an image element.

j. Assign the image src attributes to these image URLs:

Facebook

https://content.codecademy.com/projects/make-a-website/lesson-4/facebook-grey.svg

Twitter

https://content.codecademy.com/projects/make-a-website/lesson-4/twitter-grey.svg

Instagram

https://content.codecademy.com/projects/make-a-website/lesson-4/instagram-grey.svg

Medium

https://content.codecademy.com/projects/make-a-website/lesson-4/medium-grey.svg

For help, here is the exercise that introduced using Bootstrap to create a footer.

[Skip to Content](https://www.codecademy.com/courses/make-a-website/projects/codebrainery#page-skip-to-content-target)

[](https://www.codecademy.com/)

[My Home](https://www.codecademy.com/learn)

Syllabus

Connected to Codecademy

Fork

Get Unstuck

Tools

![Avatar](https://www.gravatar.com/avatar/61a4479d8b03da7eb330cff9a6ee7f28?s=140&d=retro)

# Codebrainery.io

## Project Brief

Objective

How to Make a Website with NameCheap

### Codebrainery.io

Codebrainery.io is a learn-to-code website. Let’s build their homepage using a combination of Bootstrap and custom CSS, provided by the file **style.css**.

If you get stuck during this project, check out the **project walkthrough video** which can be found in the help menu.

### Tasks

4/7 complete

Mark the tasks as complete by checking them off

## Codebrainery.io

1.

Start by linking to Bootstrap. In **index.html**, inside the head element, create a link element with an href attribute that points to:

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/cs</span><span class="mtk1">s/bootstrap.min.css</span></span><br><span><span></span></span><br></div></code></pre>
```

Stuck? Get a hint

2.

Next create the header with navbar in **index.html**.  
  
Steps:  
  
a. Start with a header element with class “container”.  
  
b. Inside the header, add a div with the class “row”.  
  
c. Inside the div, create:  

-   an h1 element with the class “col-sm-8”. Have it display the text “Codebrainery.io”.  
    
-   a nav element with a class of “col-sm-4”.  
    

d. Inside the nav, create three p elements to list navbar items: “Sign In”, “Sign Up” and “About”.

Stuck? Get a hint

3.

Now, let’s enhance the navbar with some custom CSS.  
  
a. In **index.html**, locate the `p` elements which display the navbar choices “Sign In” and “Sign Up”.  
  
b. Give the `p` that displays “Sign In” a class of “pill-white”.  
  
c. Give the `p` that displays “Sign Up” a class of “pill-black”.

The “pill-white” and “pill-black” classes are located in **style.css**. If you are curious, open the file and take a look at how those rules are implemented.

Stuck? Get a hint

4.

Now create a jumbotron section to display Codebrainery.io’s new course: Build a Website.  
  
Steps:  
  
a. In **index.html**, below the `</header>` tag, create a section element with the “jumbotron” class.  
  
b. Inside the section, add a div with the class “container”.  
  
c. Inside the div, add another div with the class “row text-center”.  
  
d. Inside the div with class “row text-center”, add an h2 element that displays the text “New Course Release”.  
  
e. Below the h2, add an h3 element that displays the text “Build a Website”.

Stuck? Get a hint

5.

Next, add a supporting content section to display the courses taught on codebrainery.io.  
  
Steps:  
  
a. In **index.html**, below the closing `</section>` tag, create another section element with a class of “container”.  
  
b. Inside the section, add two div elements, and give each a class of “row”.  
  
c. Inside each “row” div, create three figure elements, each with a class of “col-sm-4”.  
  
d. Inside each figure, add an image element containing one of the following image URLs:  
  

Ruby:

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/ruby.png</span></span><br><span><span></span></span><br></div></code></pre>
```

JavaScript:

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/javascript.png</span></span><br><span><span></span></span><br></div></code></pre>
```

MySQL:

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/mysql.png</span></span><br><span><span></span></span><br></div></code></pre>
```

PHP

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/php.png</span></span><br><span><span></span></span><br></div></code></pre>
```

jQuery

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/jquery.png</span></span><br><span><span></span></span><br></div></code></pre>
```

Python

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/python.png</span></span><br><span><span></span></span><br></div></code></pre>
```

Stuck? Get a hint

6.

Below the supporting content section add a link for the site visitor to view all courses codebrainery.io has to offer.  
  
Steps:  
  
a. To start, add a div with the class “row text-center”.  
  
b. Inside the div, add an anchor element with the class “btn btn-primary”.  
  
c. Give the anchor element an href attribute and set its value to “#”, as a placeholder for a URL.  
  
d. Have the anchor element display the text “View All Courses”.

Stuck? Get a hint

7.

Now add a footer to the bottom of the webpage. The footer will display the name of the website and links to social media sites.  
  
Steps:  
  
a. Start by creating a footer element with the class “container”.  
  
b. Inside the footer, create a div with the class “row”.  
  
c. Inside the div, create a p element and a ul element.  
  
d. Give the p element a class of “col-sm-4”.  
  
e. Have the p element display the text “codebrainery.io”.  
  
f. Give the ul a class of “col-sm-8 text-right”.  
  
g. Add four list items inside the ul.  
  
h. Give each list item a class of “col-sm-1”.  
  
i. Inside each list item, add an image element.  
  
j. Assign the image src attributes to these image URLs:

Facebook

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/facebook-grey.svg</span></span><br><span><span></span></span><br></div></code></pre>
```

Twitter

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/twitter-grey.svg</span></span><br><span><span></span></span><br></div></code></pre>
```

Instagram

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/instagram-grey.svg</span></span><br><span><span></span></span><br></div></code></pre>
```

Medium

```
<pre class="gamut-1pjy0bn e1aon2sq0"><code><div data-lang="plaintext" class="gamut-13bvm8t e5rxebe0"><span><span class="mtk1">https://content.codecademy.com/projects/make-a-web</span><span class="mtk1">site/lesson-4/medium-grey.svg</span></span><br><span><span></span></span><br></div></code></pre>
```

For help, [here is the exercise](https://www.codecademy.com/en/courses/make-a-website/lessons/bootstrap/exercises/footers) that introduced using Bootstrap to create a footer.

Stuck? Get a hint

## Code Editor

index.html

style.css

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

.jumbotron h2 {

  background-color: #FFFFFF;

  display: inline-block;

  color: #F06529;

  font-weight: 700;

  padding: 10px 35px;

  border-radius: 5px;

}

.jumbotron h3 {

  color: #FFFFFF;

  font-weight: bold;

}

.btn-primary {

  color: #2e6da4;

  background-color: #FFFFFF;

}

.col-sm-1 img {

  min-width: 32px;

  min-height: 33px;

}

Save

## Web Browser

<iframe title="Codecademy Web Browser" allowfullscreen="" class="styles_frame__MXGXK" allow="geolocation; microphone; camera" src="https://4552151f4cbb405983b9bdb021a1181a.cc-propeller.cloud/"></iframe>

4/7 complete

Back

Next


:root { --onetrust-brand-purple: #3A10E5; --onetrust-color-gray-500: #828285; --onetrust-color-white: #fff; } #onetrust-banner-sdk { padding: 1rem !important; } #onetrust-banner-sdk > .ot-sdk-container { width: 100% !important; } #onetrust-banner-sdk > .ot-sdk-container > .ot-sdk-row { display: flex !important; flex-direction: column !important; align-items: center !important; max-width: 1436px !important; margin: 0 auto !important; } #onetrust-banner-sdk > .ot-sdk-container > .ot-sdk-row:after { content: none !important; } #onetrust-group-container { display: flex !important; justify-content: center; float: none !important; width: 100% !important; max-width: 1148px !important; margin-left: 0 !important; margin-bottom: 0.625rem !important; } #onetrust-policy, #onetrust-policy-text { margin: 0 !important; font-size: 0.875rem !important; line-height: 1.375rem !important; text-align: center !important; float: none !important; } #onetrust-policy-text a { text-decoration: none; line-height: 26px !important; margin-left: 0 !important; } #onetrust-button-group-parent { position: relative !important; top: initial !important; left: initial !important; transform: initial !important; width: 264px !important; margin: 0 !important; padding: 0 !important; float: none !important; } #onetrust-button-group { display: flex !important; margin: 0 !important; } #onetrust-pc-btn-handler, #onetrust-accept-btn-handler { min-width: initial !important; padding: 0.375rem 1rem !important; margin: 0 !important; opacity: 1 !important; border-radius: 2px !important; line-height: 1.5 !important; user-select: none !important; font-size: 1rem !important; } #onetrust-pc-btn-handler:focus, #onetrust-accept-btn-handler:focus { box-shadow: 0 0 0 2px var(--onetrust-color-white), 0 0 0 4px var(--onetrust-brand-purple); text-decoration: none !important; outline: none !important; } #onetrust-pc-btn-handler{ color: var(--onetrust-brand-purple) !important; border: 1px solid var(--onetrust-brand-purple)!important; background: var(--onetrust-color-white) !important } #onetrust-accept-btn-handler { color: var(--onetrust-color-white) !important; background: var(--onetrust-brand-purple)!important; margin-left: 1rem !important; } #onetrust-close-btn-container { display: none !important; } .pc-logo { display: none !important; } #accept-recommended-btn-handler, .ot-pc-refuse-all-handler, .save-preference-btn-handler { margin-left: 4px !important; font-size: 14px !important; } #accept-recommended-btn-handler:focus, #onetrust-pc-sdk .ot-pc-refuse-all-handler:focus, #onetrust-pc-sdk .save-preference-btn-handler:focus { box-shadow: 0 0 0 2px var(--onetrust-color-white), 0 0 0 4px var(--onetrust-brand-purple); text-decoration: none !important; outline: none !important; opacity: 1 !important; } .ot-switch-label { border: 1px solid var(--onetrust-color-gray-500) !important; background-color: var(--onetrust-color-gray-500) !important; } .ot-switch-nob { background: var(--onetrust-color-white) !important; } .ot-switch-inner:before { background-color: var(--onetrust-brand-purple) !important; } .switch-checkbox:checked+.ot-switch-label .ot-switch-nob { border-color: var(--onetrust-brand-purple) !important; } .ot-pc-footer-logo { display: none !important; } #onetrust-banner-sdk>.ot-sdk-container { overflow: visible !important; } @media (max-width: 30rem) { #accept-recommended-btn-handler, .ot-pc-refuse-all-handler, .save-preference-btn-handler { width: 96% !important; } } @media (min-width: 37.5rem) { #onetrust-banner-sdk { padding: 0.875rem 1rem !important; } } @media (min-width: 48rem) { #onetrust-banner-sdk { padding: 0.875rem 1.25rem !important; } } @media (min-width: 1650px) { #onetrust-banner-sdk > .ot-sdk-container > .ot-sdk-row { flex-direction: row !important; justify-content: space-between !important; } #onetrust-group-container { margin-bottom: 0 !important; } #onetrust-button-group { flex-direction: row !important; } }

!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b.\_fbq||(b.\_fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=\[\],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)\[0\],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en\_US/fbevents.js");google\_tag\_manager\["rm"\]\["7640584"\](19)?fbq("dataProcessingOptions",\[\]):fbq("dataProcessingOptions",\["LDU"\],1,1E3);fbq("init","1036078779778355",{external\_id:google\_tag\_manager\["rm"\]\["7640584"\](20)}); fbq("track","PageView");

![](https://www.facebook.com/tr?id=1036078779778355&ev=PageView&noscript=1)

var img=document.createElement("img"),axel=Math.random()+"",a=1E13\*axel;img.src="https://ad.doubleclick.net/ddm/activity/src\\x3d12137115;type\\x3dinvmedia;cat\\x3dsitev0;dc\_lat\\x3d;dc\_rdid\\x3d;tag\_for\_child\_directed\_treatment\\x3d;tfua\\x3d;npa\\x3d;gdpr\\x3d${GDPR};gdpr\_consent\\x3d${GDPR\_CONSENT\_755};ord\\x3d"+a+"?";img.width=1;img.height=1;img.style="position: absolute;";img.ariaHidden="true";document.getElementsByTagName("body")\[0\].appendChild(img);![](https://ad.doubleclick.net/ddm/activity/src=12137115;type=invmedia;cat=sitev0;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;npa=;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755};ord=2260865681830.7437?) var amazon\_img=document.createElement("img");amazon\_img.src="https://s.amazon-adsystem.com/iui3?d\\x3dforester-did\\x26ex-fargs\\x3d%3Fid%3Dc3caf679-d643-0e37-200d-a9318093cff2%26type%3D55%26m%3D1\\x26ex-fch\\x3d416613\\x26ex-src\\x3dhttps://www.codecademy.com\\x26ex-hargs\\x3dv%3D1.0%3Bc%3D585839407104391974%3Bp%3DC3CAF679-D643-0E37-200D-A9318093CFF2";amazon\_img.width=1;amazon\_img.height=1;amazon\_img.ariaHidden="true";amazon\_img.style="position: absolute;";amazon\_img.alt="";amazon\_img.border="0";document.getElementsByTagName("body")\[0\].appendChild(amazon\_img);![](https://s.amazon-adsystem.com/iui3?d=forester-did&ex-fargs=%3Fid%3Dc3caf679-d643-0e37-200d-a9318093cff2%26type%3D55%26m%3D1&ex-fch=416613&ex-src=https://www.codecademy.com&ex-hargs=v%3D1.0%3Bc%3D585839407104391974%3Bp%3DC3CAF679-D643-0E37-200D-A9318093CFF2)(function(a,b){var d="spdt-capture",e="script";if(!b.getElementById(d)){a.spdt=a.spdt||function(){(a.spdt.q=a.spdt.q||\[\]).push(arguments)};var c=b.createElement(e);c.id=d;c.async=1;c.src="https://pixel.byspotify.com/ping.min.js";b=b.getElementsByTagName(e)\[0\];b.parentNode.insertBefore(c,b)}a.spdt("conf",{key:"d198eca79dbc41288d15d71925efa530"});a.spdt("view")})(window,document); !function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b.\_fbq||(b.\_fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=\[\],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)\[0\],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en\_US/fbevents.js");google\_tag\_manager\["rm"\]\["7640584"\](38)?fbq("dataProcessingOptions",\[\]):fbq("dataProcessingOptions",\["LDU"\],1,1E3);fbq("init","1036078779778355",{external\_id:google\_tag\_manager\["rm"\]\["7640584"\](39)}); fbq("track","PageView");

![](https://www.facebook.com/tr?id=1036078779778355&ev=PageView&noscript=1)

var img=document.createElement("img"),axel=Math.random()+"",a=1E13\*axel;img.src="https://ad.doubleclick.net/ddm/activity/src\\x3d12137115;type\\x3dinvmedia;cat\\x3dsitev0;dc\_lat\\x3d;dc\_rdid\\x3d;tag\_for\_child\_directed\_treatment\\x3d;tfua\\x3d;npa\\x3d;gdpr\\x3d${GDPR};gdpr\_consent\\x3d${GDPR\_CONSENT\_755};ord\\x3d"+a+"?";img.width=1;img.height=1;img.style="position: absolute;";img.ariaHidden="true";document.getElementsByTagName("body")\[0\].appendChild(img);![](https://ad.doubleclick.net/ddm/activity/src=12137115;type=invmedia;cat=sitev0;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;npa=;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755};ord=8377515755410.541?) var amazon\_img=document.createElement("img");amazon\_img.src="https://s.amazon-adsystem.com/iui3?d\\x3dforester-did\\x26ex-fargs\\x3d%3Fid%3Dc3caf679-d643-0e37-200d-a9318093cff2%26type%3D55%26m%3D1\\x26ex-fch\\x3d416613\\x26ex-src\\x3dhttps://www.codecademy.com\\x26ex-hargs\\x3dv%3D1.0%3Bc%3D585839407104391974%3Bp%3DC3CAF679-D643-0E37-200D-A9318093CFF2";amazon\_img.width=1;amazon\_img.height=1;amazon\_img.ariaHidden="true";amazon\_img.style="position: absolute;";amazon\_img.alt="";amazon\_img.border="0";document.getElementsByTagName("body")\[0\].appendChild(amazon\_img);![](https://s.amazon-adsystem.com/iui3?d=forester-did&ex-fargs=%3Fid%3Dc3caf679-d643-0e37-200d-a9318093cff2%26type%3D55%26m%3D1&ex-fch=416613&ex-src=https://www.codecademy.com&ex-hargs=v%3D1.0%3Bc%3D585839407104391974%3Bp%3DC3CAF679-D643-0E37-200D-A9318093CFF2)(function(a,b){var d="spdt-capture",e="script";if(!b.getElementById(d)){a.spdt=a.spdt||function(){(a.spdt.q=a.spdt.q||\[\]).push(arguments)};var c=b.createElement(e);c.id=d;c.async=1;c.src="https://pixel.byspotify.com/ping.min.js";b=b.getElementsByTagName(e)\[0\];b.parentNode.insertBefore(c,b)}a.spdt("conf",{key:"d198eca79dbc41288d15d71925efa530"});a.spdt("view")})(window,document); (function(){window.setTimeout(function(){var a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src=("https:"==document.location.protocol?"https://":"http://")+"www.lightboxcdn.com/vendor/d0c0bafe-5494-429c-b961-eaff9f61e754/lightbox.js?mb\\x3d"+(new Date).getTime();var b=document.getElementsByTagName("script")\[0\];b.parentNode.insertBefore(a,b)},500)})();

<iframe id="cuboxSaverTool" allowtransparency="true" style="
    position: fixed;
    right: 20px;
    top: 20px;
    height: 54px;
    width: 330px;
    min-height: 54px;
    min-width: 330px;
    max-height: calc(100vh - 40px);
    display: block;
    border-radius: 8px;
    overflow: hidden;
    background: transparent;
    border:none;
    pointer-events: initial;
    z-index: 100000000000000000;
    animation: 0.2s ease 0s 1 normal none running cuboxSaverTool-slide-up;
    color-scheme: light;
  " src="chrome-extension://bflmgpechpeohjfomgfdkkfcbhfcjohl/html/window.html?&amp;isSaved=false"></iframe>