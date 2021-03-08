# SystemsAnalysis
Repo for  IS3100 Systems Analysis and Design Project
if we build the site before we make the design documents, then we won't have to think much about the design documents :)

# TODO:

Development:
* [x] Initalize Django
* [x] make general template site
* [x] create database
* [x] **Article logic ( announcements are/should just be renamed articles really )**
  * [x] page for generating new articles/announcements
  * [x] page for displaying all articles/announcements
  * [x] individual article page templates
  * [x] commenting templates at the end of articles/announcements
  * [x] These bulletpoints really reduce how much work this section was, so Im adding some extra ones to make myself feel better :)
* [ ] disable django built in admin? ( because I've never used it lol)
* [ ] **email/text notifications**
  * [ ] build email/text script
  * [x] figure out how it will attach to web app (IE how does script fire, do we need a database change for it ? )
  * [ ] integrate it into web app
* [ ] admin page
* [x] initialize user accounts
* [x] user comment engine

New stuff that we need (UPDATED 3/8/21)
* [ ] style upgrade
* [ ] formatting data nicer
* [ ] notification on successful login/registration
* [ ] user permissions systems
* [ ] testing if adding and deleting things breaks stuff


Deployment:
* if we self host
  * [ ] Deploy the site
  * [ ] DNS/web
    * [ ] DNS name
    * [ ] SSL cert  
  * [ ] Do all the NGINX BS
  * [ ] update the project into PROD mode ( disable debug lol)
* Additionally, if we host on a service(skips most of nginx pain):
  * [ ] learn how the web hosting service works

# Known Bugs:

* [x] Fix logout functionality
* [ ] Various style inconsistencies
* [ ] bugs where you can submit data to an invisible form manually (Security vuln? )
