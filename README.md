  _____             _ _    _____                      
  / ____|           (_) |  / ____|                     
 | (___  _ __   __ _ _| | | |  __  __ _ _ __ ___   ___ 
  \___ \| '_ \ / _` | | | | | |_ |/ _` | '_ ` _ \ / _ \
  ____) | | | | (_| | | | | |__| | (_| | | | | | |  __/
 |_____/|_| |_|\__,_|_|_|  \_____|\__,_|_| |_| |_|\___|
                                                                                                          
### Group 3
___

The group members are:

1. Alfie Walliss
2. Hugo Hewitt
3. Curtis Wheeler
4. Joshua Foster
5. Jai Jadeja
6. Alastair Palmer-Walsh


This is a submission for Sprint 1. There are three types of document that you will find the following places.

## PROCESS DOCUMENTS
Our process documents are managed in the trello platform. The link to our project page is below. We (specific username that added) have added mattcollison2 to the board so it is visible.

trello link: [https://trello.com/b/fSaYeZM8/group-software-engineering]

We have also taken regular snapshots of the kanban board in trello to archive our progress. These are held in the repository below.

/process docs/kanban-snapshots/kanban Snapshots.pdf

Within process documents we have also included the meeting notes, agenda and minutes. These will be found in the repository below.

./process documents/meeting-notes/

## TECHNICAL DOCUMENTS
Our technical documents are primarily managed on the github system. The link to the project is below:

github link: [https://github.com/alfiewalliss/Group-Software-Project]

## PRODUCT DOCUMENTS
Our product documents are primarily in the form of a product UI. To run the program enter the technical docs directory and run the command:

python manage.py runserver

The UI and design documents for the client will be found in the repository below. 
/product docs/designs/ UI Document.jpeg

## SOFTWARE REQUIREMENTS

The software requirements for this project can be found in a text file (requirements.txt) in the following trajectory > Group-Software-Project/technical docs/requirements.txt

## HOW TO RUN TESTS

To run the tests do the following:

> Enter the trajectory Group-Software-Project/technical docs/ 
> run the command 'python manage.py test tests' to run all the tests


## ADMIN ACCOUNT

The default admin account can be access by logging in with the username 'admin' and the password 'gcd22'.

Admin permissions can be passed to different accounts by; firstly logging into an admin account, opening the settings tab, clicking 'Adjust Game Master Accounts' and typing in the username of the account to be made into an admin account.

Admin accounts have access to the following:

> Ability to change difficulties mid-game:
This can be accessed through the 'Difficulty' option in the settings tab.
By clicking on a difficulty you are able to change the speed of the snail mid-game. This can be used for testing the effectiveness of new task locations.

> Ability to edit tasks: 
This can be accessed through the 'Edit Tasks' option in the settings tab.
To add a new task click on a campus location on the map. Upon doing so, the longitude and latitude fields will be autofilled. Then all that is left to do is provide a name for the selected location and clicking submit. To remove  task location, click on one of the points on the map (blue icons), the location will be autofilled in the textbox. Then click submit to remove the selected task.

> Ability to access the github:
This can be accessed through the 'Link To Github' option in the settings tab.
Once clicked, the github repository will be opened in a new tab.

> Ability to adjust permissions for accounts:
This can be accessed through the 'Adjust Game Master Accounts' option in the settings tab.
To use this feature click on a username in the table. Once clicked the name will be autofilled into the bar beneath 'Change User Permissions'. Upon clicking 'submit' the select account will either, gain superuser permissions or lost them.


## DESCRIPTION OF GAME

The Snail Game is a test of both tactics and endurance, yet the aim of the game is relatively simple: complete as many tasks as possible and don't get caught by the snail!

On the map, there are three types of icons: player icons (showing yours and other player's locations), task icons (showing the locations of your specific tasks) and the snail icon (showing the location of the snail). This game uses your real-life location so, to complete a task, you must head to one of the task locations shown on the map.

When you start a new game, you will be greeted with the option to select what difficulty you would like to play the game at. There are 3 different abilities to pick between; easy, normal and hard. But, know that the harder you set the difficulty, the more points you get for completing a task! So your challenge is to collect as many points as you can before being caught by the dreaded snail! Do you have what it takes to defeat him? 🐌

## INSTALLATION GUIDE

There is no installation required! The game is hosted on a google cloud server. To access the game 
please visit the following link ===[GAME LINK]====

To run the game locally, move into the 'techical doc' trajectory and first run 'pip install -r requirements.txt' to install all the software requirements then run 'python manage.py runserver' in terminal (make sure all migrations are done first via 'python manage.py makemigrations' 'python manage.py migrate').

## KNOWN BUGS AND FIXES

Currently there are no known bugs within the application. If you happen to stumble across one
please content us at admin@thesnailgame.com

## FAQ

-> Q. Can task locations be changed and/or new task locations introduced.
Yes! Those with access to game master account permissions are able to manipulate tasks.

-> Q. How can I give game master permissions to accounts?
By logging into an account with game master permissions and visiting the settings tabs, click on
'Adjust Game Master Accounts'. From here, add the name of the account you would like to give/take permissions from.

-> Q. How can I score more highly?
By visiting more locations and playing on a higher difficulty you will be able to increase your score dramatically!

## COPYRIGHT AND LICIENSING INFORMATION

Terms and Conditions
Welcome to The Snail Game!

These terms and conditions outline the rules and regulations for the use of The Snail Game's Website.

By accessing this website we assume you accept these terms and conditions. Do not continue to use The Snail Game if you do not agree to take all of the terms and conditions stated on this page.

The following terminology applies to these Terms and Conditions, Privacy Statement and Disclaimer Notice and all Agreements: "Client", "You" and "Your" refers to you, the person log on this website and compliant to the Company’s terms and conditions. "The Company", "Ourselves", "We", "Our" and "Us", refers to our Company. "Party", "Parties", or "Us", refers to both the Client and ourselves. All terms refer to the offer, acceptance and consideration of payment necessary to undertake the process of our assistance to the Client in the most appropriate manner for the express purpose of meeting the Client’s needs in respect of provision of the Company’s stated services, in accordance with and subject to, prevailing law of Netherlands. Any use of the above terminology or other words in the singular, plural, capitalization and/or he/she or they, are taken as interchangeable and therefore as referring to same.

Cookies
We employ the use of cookies. By accessing The Snail Game, you agreed to use cookies in agreement with the The Snail Game's Privacy Policy.

Most interactive websites use cookies to let us retrieve the user’s details for each visit. Cookies are used by our website to enable the functionality of certain areas to make it easier for people visiting our website. Some of our affiliate/advertising partners may also use cookies.

License
Unless otherwise stated, The Snail Game and/or its licensors own the intellectual property rights for all material on The Snail Game. All intellectual property rights are reserved. You may access this from The Snail Game for your own personal use subjected to restrictions set in these terms and conditions.

You must not:

Republish material from The Snail Game
Sell, rent or sub-license material from The Snail Game
Reproduce, duplicate or copy material from The Snail Game
Redistribute content from The Snail Game
This Agreement shall begin on the date hereof. Our Terms and Conditions were created with the help of the Terms And Conditions Template.

Parts of this website offer an opportunity for users to post and exchange opinions and information in certain areas of the website. The Snail Game does not filter, edit, publish or review Comments prior to their presence on the website. Comments do not reflect the views and opinions of The Snail Game,its agents and/or affiliates. Comments reflect the views and opinions of the person who post their views and opinions. To the extent permitted by applicable laws, The Snail Game shall not be liable for the Comments or for any liability, damages or expenses caused and/or suffered as a result of any use of and/or posting of and/or appearance of the Comments on this website.

The Snail Game reserves the right to monitor all Comments and to remove any Comments which can be considered inappropriate, offensive or causes breach of these Terms and Conditions.

You warrant and represent that:

You are entitled to post the Comments on our website and have all necessary licenses and consents to do so;
The Comments do not invade any intellectual property right, including without limitation copyright, patent or trademark of any third party;
The Comments do not contain any defamatory, libelous, offensive, indecent or otherwise unlawful material which is an invasion of privacy
The Comments will not be used to solicit or promote business or custom or present commercial activities or unlawful activity.
You hereby grant The Snail Game a non-exclusive license to use, reproduce, edit and authorize others to use, reproduce and edit any of your Comments in any and all forms, formats or media.

Hyperlinking to our Content
The following organizations may link to our Website without prior written approval:

Government agencies;
Search engines;
News organizations;
Online directory distributors may link to our Website in the same manner as they hyperlink to the Websites of other listed businesses; and
System wide Accredited Businesses except soliciting non-profit organizations, charity shopping malls, and charity fundraising groups which may not hyperlink to our Web site.
These organizations may link to our home page, to publications or to other Website information so long as the link: (a) is not in any way deceptive; (b) does not falsely imply sponsorship, endorsement or approval of the linking party and its products and/or services; and (c) fits within the context of the linking party’s site.

We may consider and approve other link requests from the following types of organizations:

commonly-known consumer and/or business information sources;
dot.com community sites;
associations or other groups representing charities;
online directory distributors;
internet portals;
accounting, law and consulting firms; and
educational institutions and trade associations.
We will approve link requests from these organizations if we decide that: (a) the link would not make us look unfavorably to ourselves or to our accredited businesses; (b) the organization does not have any negative records with us; (c) the benefit to us from the visibility of the hyperlink compensates the absence of The Snail Game; and (d) the link is in the context of general resource information.

These organizations may link to our home page so long as the link: (a) is not in any way deceptive; (b) does not falsely imply sponsorship, endorsement or approval of the linking party and its products or services; and (c) fits within the context of the linking party’s site.

If you are one of the organizations listed in paragraph 2 above and are interested in linking to our website, you must inform us by sending an e-mail to The Snail Game. Please include your name, your organization name, contact information as well as the URL of your site, a list of any URLs from which you intend to link to our Website, and a list of the URLs on our site to which you would like to link. Wait 2-3 weeks for a response.

Approved organizations may hyperlink to our Website as follows:

By use of our corporate name; or
By use of the uniform resource locator being linked to; or
By use of any other description of our Website being linked to that makes sense within the context and format of content on the linking party’s site.
No use of The Snail Game's logo or other artwork will be allowed for linking absent a trademark license agreement.

iFrames
Without prior approval and written permission, you may not create frames around our Webpages that alter in any way the visual presentation or appearance of our Website.

Content Liability
We shall not be hold responsible for any content that appears on your Website. You agree to protect and defend us against all claims that is rising on your Website. No link(s) should appear on any Website that may be interpreted as libelous, obscene or criminal, or which infringes, otherwise violates, or advocates the infringement or other violation of, any third party rights.

Your Privacy
Privacy Policy
Last updated: March 16, 2022

This Privacy Policy describes Our policies and procedures on the collection, use and disclosure of Your information when You use the Service and tells You about Your privacy rights and how the law protects You.

We use Your Personal data to provide and improve the Service. By using the Service, You agree to the collection and use of information in accordance with this Privacy Policy. This Privacy Policy has been created with the help of the Privacy Policy Template.

Interpretation and Definitions
Interpretation
The words of which the initial letter is capitalized have meanings defined under the following conditions. The following definitions shall have the same meaning regardless of whether they appear in singular or in plural.

Definitions
For the purposes of this Privacy Policy:

Account means a unique account created for You to access our Service or parts of our Service.

Company (referred to as either "the Company", "We", "Us" or "Our" in this Agreement) refers to The Snail Game, Exeter Universite.

Cookies are small files that are placed on Your computer, mobile device or any other device by a website, containing the details of Your browsing history on that website among its many uses.

Country refers to: United Kingdom

Device means any device that can access the Service such as a computer, a cellphone or a digital tablet.

Personal Data is any information that relates to an identified or identifiable individual.

Service refers to the Website.

Service Provider means any natural or legal person who processes the data on behalf of the Company. It refers to third-party companies or individuals employed by the Company to facilitate the Service, to provide the Service on behalf of the Company, to perform services related to the Service or to assist the Company in analyzing how the Service is used.

Usage Data refers to data collected automatically, either generated by the use of the Service or from the Service infrastructure itself (for example, the duration of a page visit).

Website refers to The Snail Game, accessible from http://127.0.0.1:8000/

You means the individual accessing or using the Service, or the company, or other legal entity on behalf of which such individual is accessing or using the Service, as applicable.

Collecting and Using Your Personal Data
Types of Data Collected
Personal Data
While using Our Service, We may ask You to provide Us with certain personally identifiable information that can be used to contact or identify You. Personally identifiable information may include, but is not limited to:

Email address

First name and last name

Usage Data

Usage Data
Usage Data is collected automatically when using the Service.

Usage Data may include information such as Your Device's Internet Protocol address (e.g. IP address), browser type, browser version, the pages of our Service that You visit, the time and date of Your visit, the time spent on those pages, unique device identifiers and other diagnostic data.

When You access the Service by or through a mobile device, We may collect certain information automatically, including, but not limited to, the type of mobile device You use, Your mobile device unique ID, the IP address of Your mobile device, Your mobile operating system, the type of mobile Internet browser You use, unique device identifiers and other diagnostic data.

We may also collect information that Your browser sends whenever You visit our Service or when You access the Service by or through a mobile device.

Tracking Technologies and Cookies
We use Cookies and similar tracking technologies to track the activity on Our Service and store certain information. Tracking technologies used are beacons, tags, and scripts to collect and track information and to improve and analyze Our Service. The technologies We use may include:

Cookies or Browser Cookies. A cookie is a small file placed on Your Device. You can instruct Your browser to refuse all Cookies or to indicate when a Cookie is being sent. However, if You do not accept Cookies, You may not be able to use some parts of our Service. Unless you have adjusted Your browser setting so that it will refuse Cookies, our Service may use Cookies.
Flash Cookies. Certain features of our Service may use local stored objects (or Flash Cookies) to collect and store information about Your preferences or Your activity on our Service. Flash Cookies are not managed by the same browser settings as those used for Browser Cookies. For more information on how You can delete Flash Cookies, please read "Where can I change the settings for disabling, or deleting local shared objects?" available at https://helpx.adobe.com/flash-player/kb/disable-local-shared-objects-flash.html#main_Where_can_I_change_the_settings_for_disabling__or_deleting_local_shared_objects_
Web Beacons. Certain sections of our Service and our emails may contain small electronic files known as web beacons (also referred to as clear gifs, pixel tags, and single-pixel gifs) that permit the Company, for example, to count users who have visited those pages or opened an email and for other related website statistics (for example, recording the popularity of a certain section and verifying system and server integrity).
Cookies can be "Persistent" or "Session" Cookies. Persistent Cookies remain on Your personal computer or mobile device when You go offline, while Session Cookies are deleted as soon as You close Your web browser. Learn more about cookies: Use of Cookies by Free Privacy Policy.

We use both Session and Persistent Cookies for the purposes set out below:

Necessary / Essential Cookies

Type: Session Cookies

Administered by: Us

Purpose: These Cookies are essential to provide You with services available through the Website and to enable You to use some of its features. They help to authenticate users and prevent fraudulent use of user accounts. Without these Cookies, the services that You have asked for cannot be provided, and We only use these Cookies to provide You with those services.

Cookies Policy / Notice Acceptance Cookies

Type: Persistent Cookies

Administered by: Us

Purpose: These Cookies identify if users have accepted the use of cookies on the Website.

Functionality Cookies

Type: Persistent Cookies

Administered by: Us

Purpose: These Cookies allow us to remember choices You make when You use the Website, such as remembering your login details or language preference. The purpose of these Cookies is to provide You with a more personal experience and to avoid You having to re-enter your preferences every time You use the Website.

For more information about the cookies we use and your choices regarding cookies, please visit our Cookies Policy or the Cookies section of our Privacy Policy.

Use of Your Personal Data
The Company may use Personal Data for the following purposes:

To provide and maintain our Service, including to monitor the usage of our Service.

To manage Your Account: to manage Your registration as a user of the Service. The Personal Data You provide can give You access to different functionalities of the Service that are available to You as a registered user.

For the performance of a contract: the development, compliance and undertaking of the purchase contract for the products, items or services You have purchased or of any other contract with Us through the Service.

To contact You: To contact You by email, telephone calls, SMS, or other equivalent forms of electronic communication, such as a mobile application's push notifications regarding updates or informative communications related to the functionalities, products or contracted services, including the security updates, when necessary or reasonable for their implementation.

To provide You with news, special offers and general information about other goods, services and events which we offer that are similar to those that you have already purchased or enquired about unless You have opted not to receive such information.

To manage Your requests: To attend and manage Your requests to Us.

For business transfers: We may use Your information to evaluate or conduct a merger, divestiture, restructuring, reorganization, dissolution, or other sale or transfer of some or all of Our assets, whether as a going concern or as part of bankruptcy, liquidation, or similar proceeding, in which Personal Data held by Us about our Service users is among the assets transferred.

For other purposes: We may use Your information for other purposes, such as data analysis, identifying usage trends, determining the effectiveness of our promotional campaigns and to evaluate and improve our Service, products, services, marketing and your experience.

We may share Your personal information in the following situations:

With Service Providers: We may share Your personal information with Service Providers to monitor and analyze the use of our Service, to contact You.
For business transfers: We may share or transfer Your personal information in connection with, or during negotiations of, any merger, sale of Company assets, financing, or acquisition of all or a portion of Our business to another company.
With Affiliates: We may share Your information with Our affiliates, in which case we will require those affiliates to honor this Privacy Policy. Affiliates include Our parent company and any other subsidiaries, joint venture partners or other companies that We control or that are under common control with Us.
With business partners: We may share Your information with Our business partners to offer You certain products, services or promotions.
With other users: when You share personal information or otherwise interact in the public areas with other users, such information may be viewed by all users and may be publicly distributed outside.
With Your consent: We may disclose Your personal information for any other purpose with Your consent.
Retention of Your Personal Data
The Company will retain Your Personal Data only for as long as is necessary for the purposes set out in this Privacy Policy. We will retain and use Your Personal Data to the extent necessary to comply with our legal obligations (for example, if we are required to retain your data to comply with applicable laws), resolve disputes, and enforce our legal agreements and policies.

The Company will also retain Usage Data for internal analysis purposes. Usage Data is generally retained for a shorter period of time, except when this data is used to strengthen the security or to improve the functionality of Our Service, or We are legally obligated to retain this data for longer time periods.

Transfer of Your Personal Data
Your information, including Personal Data, is processed at the Company's operating offices and in any other places where the parties involved in the processing are located. It means that this information may be transferred to — and maintained on — computers located outside of Your state, province, country or other governmental jurisdiction where the data protection laws may differ than those from Your jurisdiction.

Your consent to this Privacy Policy followed by Your submission of such information represents Your agreement to that transfer.

The Company will take all steps reasonably necessary to ensure that Your data is treated securely and in accordance with this Privacy Policy and no transfer of Your Personal Data will take place to an organization or a country unless there are adequate controls in place including the security of Your data and other personal information.

Disclosure of Your Personal Data
Business Transactions
If the Company is involved in a merger, acquisition or asset sale, Your Personal Data may be transferred. We will provide notice before Your Personal Data is transferred and becomes subject to a different Privacy Policy.

Law enforcement
Under certain circumstances, the Company may be required to disclose Your Personal Data if required to do so by law or in response to valid requests by public authorities (e.g. a court or a government agency).

Other legal requirements
The Company may disclose Your Personal Data in the good faith belief that such action is necessary to:

Comply with a legal obligation
Protect and defend the rights or property of the Company
Prevent or investigate possible wrongdoing in connection with the Service
Protect the personal safety of Users of the Service or the public
Protect against legal liability
Security of Your Personal Data
The security of Your Personal Data is important to Us, but remember that no method of transmission over the Internet, or method of electronic storage is 100% secure. While We strive to use commercially acceptable means to protect Your Personal Data, We cannot guarantee its absolute security.

Children's Privacy
Our Service does not address anyone under the age of 13. We do not knowingly collect personally identifiable information from anyone under the age of 13. If You are a parent or guardian and You are aware that Your child has provided Us with Personal Data, please contact Us. If We become aware that We have collected Personal Data from anyone under the age of 13 without verification of parental consent, We take steps to remove that information from Our servers.

If We need to rely on consent as a legal basis for processing Your information and Your country requires consent from a parent, We may require Your parent's consent before We collect and use that information.

Location Services
This product does use location services however, all location processing is secure and is always local to you. You location will never be shared to us across a network.

Links to Other Websites
Our Service may contain links to other websites that are not operated by Us. If You click on a third party link, You will be directed to that third party's site. We strongly advise You to review the Privacy Policy of every site You visit.

We have no control over and assume no responsibility for the content, privacy policies or practices of any third party sites or services.

Changes to this Privacy Policy
We may update Our Privacy Policy from time to time. We will notify You of any changes by posting the new Privacy Policy on this page.

We will let You know via email and/or a prominent notice on Our Service, prior to the change becoming effective and update the "Last updated" date at the top of this Privacy Policy.

You are advised to review this Privacy Policy periodically for any changes. Changes to this Privacy Policy are effective when they are posted on this page.

Contact Us
If you have any questions about this Privacy Policy, You can contact us:

By email: aw840@exeter.ac.uk
Reservation of Rights
We reserve the right to request that you remove all links or any particular link to our Website. You approve to immediately remove all links to our Website upon request. We also reserve the right to amen these terms and conditions and it’s linking policy at any time. By continuously linking to our Website, you agree to be bound to and follow these linking terms and conditions.

Removal of links from our website
If you find any link on our Website that is offensive for any reason, you are free to contact and inform us any moment. We will consider requests to remove links but we are not obligated to or so or to respond to you directly.

We do not ensure that the information on this website is correct, we do not warrant its completeness or accuracy; nor do we promise to ensure that the website remains available or that the material on the website is kept up to date.

Disclaimer
To the maximum extent permitted by applicable law, we exclude all representations, warranties and conditions relating to our website and the use of this website. Nothing in this disclaimer will:

limit or exclude our or your liability for death or personal injury;
limit or exclude our or your liability for fraud or fraudulent misrepresentation;
limit any of our or your liabilities in any way that is not permitted under applicable law; or
exclude any of our or your liabilities that may not be excluded under applicable law.
The limitations and prohibitions of liability set in this Section and elsewhere in this disclaimer: (a) are subject to the preceding paragraph; and (b) govern all liabilities arising under the disclaimer, including liabilities arising in contract, in tort and for breach of statutory duty.

As long as the website and the information and services on the website are provided free of charge, we will not be liable for any loss or damage of any nature.