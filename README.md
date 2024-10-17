# SHUHAI-Book-Management-System

#### Introduction

This intelligent book borrowing system provides convenient book search, borrowing, and information maintenance functions for teachers and students at the school. Through this system, users can easily browse the library's collection, search for information about the books they need, and perform online borrowing operations. At the same time, the system also features information maintenance functions, including user personal information management and library collection management, ensuring the effective management and utilization of library resources.

It is an intelligent book borrowing system based on the Flask framework, designed to improve the service efficiency of the school library and provide a more convenient and efficient borrowing experience for teachers and students, further promoting the development of the school’s educational and teaching undertakings.

#### Software Architecture
Flask + Layui frontend UI framework + MySQL

[Layui Documentation](http://layui.xhcen.com/doc/doc.html)

#### Installation Tutorial

1.  Clone the project using git or download the zip file.
2.  Use pip to install the required packages by following the requirements file in the terminal.
3.  Install the MySQL database and related pymysql package.
4.  Open the terminal, navigate to the project folder, and start the service by running `python app.py runserver`.
5.  Open the browser and enter (http://127.0.0.1:5000) to view the system.

#### Overall Functional Requirements and Goals

![Intelligent Book Borrowing System Frontend Composition](static/%E6%99%BA%E8%83%BD%E5%9B%BE%E4%B9%A6%E5%80%9F%E9%98%85%E7%B3%BB%E7%BB%9F%E5%89%8D%E5%8F%B0%E7%BB%84%E6%88%90.png)

##### System Frontend Composition
1.  **User Login/Registration Module**: Allows users to create accounts and log in to the system.
2.  **User Center Module**: Users can view their account details, such as borrowing history and personal information.
3.  **Book Search Module**: Provides a search function that allows users to search for books by keywords, author, ISBN, etc., making it easier for readers to quickly and accurately find their borrowing targets.
4.  **Book Display Module**: Displays detailed information about the library's collection on the main interface, including cover, synopsis, author, etc., allowing readers to get an overview of the collection.
5.  **Book Borrowing Module**: The core function, allowing users to borrow books, check borrowing status, and view due dates.
6.  **Book Return Module**: Users can return books in this module. Readers return books via a special window where administrators check the book. The administrator scans the book's QR code for archiving, and readers pay any penalty fees for overdue or damaged books.
7.  **Book Recommendation Module**: Recommends related books based on users' borrowing and search history.
8.  **News/Announcements Module**: Publishes news and announcements from the library, which may include reader feedback and inquiries.
9.  **Help/FAQ Module**: Provides answers to frequently asked questions and user guides for the system.

##### System Backend Composition
![Intelligent Book Borrowing System Backend Composition](static/%E6%99%BA%E8%83%BD%E5%9B%BE%E4%B9%A6%E5%80%9F%E9%98%85%E7%B3%BB%E7%BB%9F%E5%90%8E%E5%8F%B0%E7%BB%84%E6%88%90.png)

1.  **Admin Login Module**: Administrators log in to the backend management system.
2.  **Book Management Module**: Add, edit, and delete book information.
3.  **User Management Module**: Manage user accounts, including permission assignments and user bans.
4.  **Borrowing Management Module**: View and manage users' borrowing records and statuses.
5.  **Data Statistics Module**: Generate reports on book borrowing and user activity.
6.  **System Settings Module**: Configure system parameters such as book categories and library rules.
7.  **News/Announcements Management Module**: Publish and manage system news and announcements.
8.  **Help/FAQ Management Module**: Manage help documents and frequently asked questions.
9.  **Security and Maintenance Module**: Includes database backups and viewing system logs.

#### Contributing

1.  Fork this repository.
2.  Create a new branch named Feat_xxx.
3.  Commit your code.
4.  Create a new Pull Request.