# WebDecode - Web

## Description

Do you know how to use the web inspector? Start searching [here]() to find the flag.

#### Hints:

- Use the web inspector on other files included by the web page.
- The flag may or may not be encoded.

## Solution

The link opens up to a webpage that looks like the following...

![image](./home.png)

The "ABOUT" and "CONTACT" pages look like the following...

Contact:

![image](./contact.png)

About:

![image](./about.png)

At first, they don't seem like much but after inspecting the pages, we find something interesting in the html code of the ABOUT page...

```html
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <link href="style.css" rel="stylesheet"/>
  <link href="img/favicon.png" rel="shortcut icon" type="image/x-icon"/>
  <!-- font (google) -->
  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&amp;display=swap" rel="stylesheet"/>
  <title>
   About me
  </title>
 </head>
 <body>
  <header>
   <nav>
    <div class="logo-container">
     <a href="index.html">
      <img alt="logo" src="img/binding_dark.gif"/>
     </a>
    </div>
    <div class="navigation-container">
     <ul>
      <li>
       <a href="index.html">
        Home
       </a>
      </li>
      <li>
       <a href="about.html">
        About
       </a>
      </li>
      <li>
       <a href="contact.html">
        Contact
       </a>
      </li>
     </ul>
    </div>
   </nav>
  </header>
  <section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDJjZGNiNTl9">
   <h1>
    Try inspecting the page!! You might find it there
   </h1>
   <!-- .about-container -->
  </section>
  <!-- .about -->
  <section class="why">
   <footer>
    <div class="bottombar">
     Copyright © 2023 Your_Name. All rights reserved.
    </div>
   </footer>
  </section>
 </body>
</html>
```

There seems to be a Base64 encoded text in there. A quick decode reveals the flag.

```bash

```
