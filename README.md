# SHiFT

## Project Goals
It'll workout is a web application that will allow its users to join a community of subscribers, purchase exercise/meal plans and products. 

## User Goals
All users to be able to browse packages to subscribe to and purchase products.

Subscribers can join a community, so they can access support and guidance from other users.

Standard subscribers to have access to a monthly exercise plan that updates every month.

Elite subscribers to have access to the exercise plan, a monthly meal plan and an invite to the monthly Q & A sessions.

## Business & Development Goals
To generate an income from subscriptions and products.

## User Stories

### Shopper
**Viewing & navigation**
*	I want to be able to view individual products so that I can look at the price, descriptions and reviews.
*	I want to be able to easily view my basket total so that I can keep track of how much I'm spending.

![View Products](/media/all.products.jpg)
![View Product Details](/media/product.details.jpg)
![View Basket](/media/Basket.jpg)

**Sorting & Searching**
*	I want to be able to sort the list of available products so that I can find the best rated, best priced and categorically sort products.
*	I want to be able to sort a specific category of availabe products so that I can Find the best rated, best priced in a specific category or sort products in that category by name.
*	I want to be able to sort multiple categories of products simultaneously so that I can find the best priced or best reated products across broad categories, such as supplements or equipment.
*	I want to be able to easily see what I've searched for so that I can quickly decide whether the product I want is available.
*	I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.

![Sort alphabetically](/media/sort.alpha.jpg)
![Sort categorically](/media/sort.category.jpg)
![Sort price](/media/sort.price.jpg)
![clothes](/media/clothes.jpg)
![Equipment](/media/equipment.jpg)
![supplements](/media/supplements.jpg)

**Purchasing & Checkout**
*	I want to be able to select the quantity of a product when purchasing it so that I can ensure I get how much I need.

![Checkout](/media/checkout.jpg)
![Checkout Summary](/media/checkout.summary.jpg)

### Site Users
**Viewing & navigation**
*	I want to be able to view a list of my posts and conversations so that I can I want to be able to  so that I can easily track what I've posted.
*	I want to be able to view posts of the community so that I can  page keep up to date with the community.
*	I want to be able to  so that I can .

![Community Home](/media/community.jpg)

**Registration & User Account**
*	I want to be able to register for an account so that I can have a personal account and to view my profile.
*	I want to be able to login or logout so that I can access my personal account information.
*	I want to be able to recover password if I forget so that I can recover access to my account.
*	I want to be able to receive an email confirming a successful registration so that I can verify that I have registered successfully.
*	I want to be able to have a user profile so that I can view my order history, confirmations, save my payment info.
*   I want to be able see the customer reviews so that I can make an informed choice to purchase a product.
*   I want to be able to create product review so that I can share my experiences with others that use the site.

![Register](/media/registration.jpg)
![Sign Out](/media/sign.out.jpg)
![Log Out](/media/sign.out.jpg)
![Reset Password](/media/reset.password.jpg)
![Password Reset Confirm](/media/password.reset.confirm.jpg)
![Verify Password](/media/verify.email..jpg)
![Confirm Email](/media/confirm.email.jpg)
![Change Password](/media/change.password.jpg)
![Profile](/media/profile.personal.jpg)
![Profile Orders](/media/profile.order.jpg)
![Review](/media/prod.det.review.jpg)
![Customer Reviews](/media/prod.det.review.jpg)
![Sort price](/media/review.form.jpg)


**Sorting & Searching**
*	I want to be able to search for other community users by name or location so that I can see what information they are providing.

![Search Posts](/media/search.post.jpg)

**Community**
*	I want to be able to post a blog so that I can upload a photo and share my experience with the community.
*	I want to be able to comment on a blog so that I can share my support for that person.
*	I want to be able to rate a product and write a review so that I can support without having to post a comment.
*	
![Post](/media/post.jpg)
![Edit Post]()
![Comment](/media/comment.jpg)
![Edit Comment](/media/edit.commit.jpg)

## Future Features
* User will have the option to pick from multiple plans in exchange for a higher subscribtion fee.
* User will be able to sign up to a subscription package where they will get montly Exercise and Meal Plans.
* Private messaging between connected subscribers
* Users will be able to customise their profiles.
## Typography & Colour
*	Caveat has been used for the font.
*	Bootstrap colour scheme has been used to for the follow:
	*	text-danger and text-black for the logo.
	*	text-dark and text-white for the buttons.
	*	text-danger and text-info for the checkout bag.
	*	bg-light for the background colour
	*	text-black, text-white and text-muted for the font.
*	#ffc107 (Yellow) for the review stars.

## Wireframes
![Base Template](/media/base.html.jpg)
![Home Page](/media/home.wf.jpg)
[Products](/media/products.wf.jpg)
![Product detail](/media/product.details.wf.jpg)
![Checkout](/media/checkout.wf.jpg)
![Checkout Summary](/media/checkout.summary.wf.jpg)
![Basket](/media/basket.wf.jpg)
![Profile](/media/profile.wf.jpg)
![Reviews](/media/reviews.wf.jpg)
![Sign In](/media/sign-in.wf.jpg)
![Register](/media/register.wf.jpg)
![Community](/media/community.wf.jpg)

## Technology

- [Codeanywhere](https://app.codeanywhere.com/) to build the repository.
- [GitHub](https://github.com/Code-Institute-Org/ci-full-template) to push changes to the repository.
- [Heroku](https://id.heroku.com/login) to deploy the application.HTML and CSS code
- [jslint](https://www.jslint.com/) to validate JavaScript code.
- [Balsamiq](https://balsamiq.com/) for creating the wireframe
- [Font Awesome](https://fontawesome.com/v4/) for the icons
- [Google fonts](https://fonts.google.com/) to search for the right fonts for the website
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)  to create forms and buttons.
- Chrome Developer Tools for device testing.

## Testing
### Code Validation
### Test Cases
**Home page**

When the user first visits the home page...
When the user clicked on the logo does it refreshed the page?
*The page is refreshed when the user clicks on the logo*

When the "Shop Now" button on the home page is pushed does it render the all products page?
*When the shop now button is pressed it rendered the all products page*

On the second carousel does the text on the button change when the user is registered?
*The text on the button changes from "sign up" to "talk to us" when the user is registered.*

On the second carousel does the button render a differ page if the user is registered?
*The button renders the register page for unregistered user and the button renders the community page when the user is registered.*

**All Products page**

When the user clicks on a product does it render the product details page?
*When the user clicks on a product is does render the products detail page with that specific product*

As the user scrolls down the page is the back to top button visible?
*When the scrolls down the page there is a button that when pushed takes returns the user to the top of the page.*

**Product details page**

When an unregistered user views the page do they have access to the review form?
*No, there is no review form*

When a registered user views the page do they have access to the review form?
*Yes, the review form is accessible*

When a user hovers over the review section are they encouraged to leave a review?
*No, only registered users are encouraged to leave a review*

When registered user clicks on the reviews section does it transport them further down page to the review section?
*Yes, when clicked the user is transported further down page so they can leave a review*

When the user hovers over the stars in the review form do they change color?
*When the user hovers over the stars in the review form the stars change for dark grey to yellow until clicked, then they are fixed depending on where the user clicked*

When the user pushed the + and - does they toggle the number to go up and down?
*Yes numbers go up and down in relation to which button was pressed.*

When the user completes the review form can is the review displayed lower down the page?
*When the review is completed the page is refreshed and the review shows up further down the page*

When the user adds a product to the bag do they receive a notification letting them know they have added something to the bag?
*Yes when the user pushes add to bag the user received a notification telling them so*

When the user pushes keep shopping are they transported back to the all products page?
*The user is transported back to the all products page when the keep shopping button is pressed*

When the user adds products to the basket that are equal to or over £50 doe the bag in the top right corner change from red to green?
*The bag changes from red to green when the value of the basket is equal to over £50.*

Can all registered users edit or delete all reviews?
*Only the auther of the reviews has access to the edit or delete button*

**Bag Page**

When the user clicks on the keep shopping button does it render the all products page?
*The user is transported to the all products page when the keep shopping button is pressed.*

When the user clicks on secure checkout does it render the checkout page?
*The checkout page is rendered when the user clicks secure checkout.*

When the users subtotal is below £50 does is the 10% service reflected in the totals section?
*The 10% service charge is applied when the users subtotal is below £50.*

When the user presses remove is the product removed from the basket?
*The product is removed from the basket when the remove button is pressed*

When the user toggles the - & + buttons and then presses update does it update the basket total?
*The basket total is updated when the - & + buttons are pressed followed by the update button*

**Checkout Page**

When the user has successfully entered their personal and card details and presses complete order does this render the checkout summary page?
*The checkout summary page is rendered once the user presses complete order.*

When the user presses the adjust bag button are they transported back to the shopping bag page?
*The user is transported back to the shopping bag page when the adjust bag button is pressed.*

**Community Page**

When a user presses the share your thoughts button is the post page rendered?
*The post page is rendered when the user presses the share your thoughts button*

When the makes a post is the post displayed on the community page?
*The users post is displayed on the community page when a post is submitted*

When the user has completed a post do they have access to the edit and delete buttons?
*The has access to the edit and delete button after they complete a post. The edit and delete button will show up only if the user is the author of the post*

Do all registered users have access to the comments button?
*All registered users have access to the comments button*

When the comments button is pressed does is render the comments page?
*The comments page is rendered when comments button is pressed*

When the user leaves a comment does it show up underneath the post that it relates too?
*The users comment is visible underneath the post that it relates to when they leave a comment*

Do all users have access to the edit and delete comment buttons?
*Only the author of the comment has access to the edit and delete buttons *

When the home button is pressed does it render the home page.
*The home page is rendered when the user clicks on the home button*

When logo is pressed does it refresh the community page?
*The community page is refreshed when the user presses the logo.*

**Profile**

When the user types in their details and presses the update button does it refresh the page with the updated details.
*The page is refreshed with the updated user details when the update button is pressed.*

If the user has made a purchase before and have checked "save details" on the checkout page are the users details prepopulated?
*The users details are prepopulated if the user has checked "save details" on the checkout page.*

When the user presses the order history tab does it toggle the order the history details?
*The order details are displayed when the order history tab is toggled.*

When the user presses the personal details tab does it toggle the personal details.
*The users personal details is displayed when the personal details tab in toggled. *

**Navigation**

Unregistered users

When search button is pushed does it toggle the search bar?
*When the search button is pushed it does toggle a search bar*

When the user pushes the my account button does it toggle options Register and Login?
*When the my accounts button is pushed it does toggle two options. Register and Login*

Registered users

When the my account button is pushed does it toggle dropdown a menu with Community, Profile and Sign Out?
*The options that are displayed with the my account button is pushed are Community, Profile and Sign Out*

When the Community option is selected from the my account menu does it render the community page?
*The community page is rendered when the community option is selected from the my account menu.*

When the profile option is selected from the my account menu does it render the profile page?
*The profile page is rendered when the profile option is selected from the my account menu.*

When the sign out option is selected from the my account menu does it render the sign out page?
*The sign out page is rendered when the sign out option is selected from the my account menu.*

When the all products option is selected from the my the navigation bar does it toggle a dropdown menu with price, categories and all products?
*The options that are displayed when the my account button is select are price, categories and all products.*

When the user selects price from the all products menu does it render the all products page in order of price?
*The all products page is rendered in order of price when the price option is selected from the all products menu.*

When the user selects categories from the all products menu does it render the all products page in order of category?
*The all products page is rendered in order of categories when the categories option is selected from the all products menu.*

When the user selects all products from the all products menu does it render the all products page?
*The all products page is rendered when the all products option is selected from the all products menu.*

When the supplements option is selected from the my the navigation bar does it render the supplements page?
*The supplements page is rendered when the supplements option is selected.*

When the equipment's option is selected from the navigation bar does it render the equipment's page?
*The equipment'	s page is rendered when the equipment's option is selected.*

When the clothes option is selected from the navigation bar does it toggle a dropdown menu with men and women?
*The options that are displayed when the my account button is select are men and women.*

When the mens option is selected from the clothes menu in the navigation bar does it render the page with only mens clothes?
*The mens clothes page is rendered when the mens clothes option is selected.*

When the womens option is selected from the clothes menu in the navigation bar does it render the page with only womens clothes?
*The womens clothes page is rendered when the womens clothes option is selected.*

When the all products option is selected from the my the navigation bar does it render the community page?
*The community page is rendered when the community option is selected from the my account menu.*
### Test Procedure
I employed a manual test procedure that involved a series of questions about the websites based on the user stories.
### Device Testing
#### 1024
![1024](/media/1024.jpg)
#### 820
![820](/media/820.jpg)
#### 768
![768](/media/768.jpg)
#### 540
![540](/media/540.jpg)
#### 430
![430](/media/430.jpg)
#### 390
![390](/media/390.jpg)
#### 280
![280](/media/280.jpg)
### Fixed Bugs
Early on I wanted to create a carousel on the home page, but bootstrap only tell how to do it with the <img> tag. I went on YouTube and searched carousel images. I found a very helpful video called "Carousel Responsive Images". This video helped me to put the images in the CSS and style them separate. Although it very common to this it this way, I needed the video just to remind me. [Carousel Video](https://www.youtube.com/watch?v=aCRs_wQAhm0&t=316s)

I wanted to create a start rating system for the users to review the products, but it didn't know where to start. I eventually searched star reviews on youtube and came across a guy call Rathan Kumer. I watched the 4 videos that he post which greatly helped me. [YouTube Video](https://youtu.be/Zkmu93lMLPs?si=tgyr2me_NyLLauK_)

### Browser Testing
#### Chrome
![Home](/media/chrome.home.jpg)
![Registration](/media/chrome.reg.jpg)
![Sign In](/media/chrome.sign.in.jpg)
![All Products](/media/chrome.prod.jpg)
![Product Details](/media/chrome.prod.det.jpg)
![Bag](/media/chrome.bag.jpg)
![Checkout](/media/chrome.checkout.jpg)
![Checkout Summary](/media/chrome.check.sum.jpg)
![Profile](/media/chrome.profile.jpg)
![Community](/media/chrome.com.jpg)
![Sign Out](/media/chrome.sign.out.jpg)

#### Edge
![Home](/media/edge.home.jpg)
![Registration](/media/edge.reg.jpg)
![Sign In](/media/edge.sign.in.jpg)
![All Products](/media/edge.prod.jpg)
![Product Details](/media/edge.prod.det.jpg)
![Bag](/media/edge.bag.jpg)
![Checkout](/media/edge.checkout.jpg)
![Checkout Summary](/media/edge.check.sum.jpg)
![Profile](/media/edge.profile.jpg)
![Community](/media/edge.com.jpg)
![Sign Out](/media/edge.sign.out.jpg)
#### FireFox
![Home](/media/fire.home.jpg)
![Registration](/media/fire.reg.jpg)
![Sign In](/media/fire.sign.in.jpg)
![All Products](/media/fire.prod.jpg)
![Product Details](/media/fire.prod.det.jpg)
![Bag](/media/fire.bag.jpg)
![Checkout](/media/fire.checkout.jpg)
![Checkout Summary](/media/fire.check.sum.jpg)
![Profile](/media/fire.profile.jpg)
![Community](/media/fire.com.jpg)
![Sign Out](/media/sign.out.jpg)
#### Opera
![Home](/media/opera.home.jpg)
![Registration](/media/opera.reg.jpg)
![Sign In](/media/op.sign.in.jpg)
![All Products](/media/opera.prod.jpg)
![Product Details](/media/opera.prod.det.jpg)
![Bag](/media/op.bag.jpg)
![Checkout](/media/op.checkout.jpg)
![Checkout Summary](/media/op.chec.sum.jpg)
![Profile](/media/op.profile.jpg)
![Community](/media/op.com.jpg)
![Sign Out](/media/op.sign.out.jpg)
## Deployment
### Codeanywhere
 1. Go to [https://app.codeanywhere.com/](https://app.codeanywhere.com/)
 2. In the Workspaces section click on “2ndborn-shift-79eiaytri6”. 
![codeanywhere workspace](/media/code1.jpg)
 3. Once the page is loaded open a new terminal and type “python3 manage.py runserver”. Then press Enter.
![terminal](/media/code2.jpg)
 4. Options to open the preview page or the browser will be shown. Click on the browser.
![port options](/media/code3.jpg)
 5. The browser will open.
![webpage](/media/code4.jpg)
### Heroku
1. Go to [Heroku.com ](https://id.heroku.com/login)
![heroku_webpage](/media/hero0.jpg)
2. From the home page find the application "shft-v1" and click on it.
![heroku_homepage](/media/hero1.jpg)
3.	Click on the deploy tab.
![deploy_tab](/media/hero2.jpg)
4. Scroll down to deployment method, click on GitHub, search for your repository profile, key in the name of the repository and then press search. ![heroku_install](/media/hero3.jpg)
5. Once the repository has been found click on connect. This will initially the install process.![heroku_install](/media/hero4.jpg)
6. Once installation has been completed, press enable automatic deploy.
![heroku_enable](/media/hero5.jpg)
7. Press deploy.
![heroku_press_deloy](/media/hero6.jpg)
8. Finally, click on the Open App button at the top of the page.
![heroku_open_app](/media/hero7.jpg)