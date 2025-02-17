<p align="center">
 <img alt="Files Logo" <img src="files/banner.png" width="450">
 <h2 align="center">WinRice - Set up your Windows device using automation
</h2>
</p>

<p align="center">
<img alt="No. of downloads" src="https://img.shields.io/github/downloads/pratyakshm/WinRice/total">  <img alt="GitHub issues" src="https://img.shields.io/github/issues/pratyakshm/WinRice">   <img alt="Platform support" src="https://img.shields.io/badge/Windows%2011-Ready-blue?&logo=windows11">  <img alt="Platform support" src="https://img.shields.io/badge/Windows%2010-Ready-blue?&logo=windows">
</p>

<p align="center">
<a href="#core-features">Features</a> &bull; 
<a href="doc">Documentation</a> &bull; 
<a href="doc/Frequently-answered-questions.md">FAQ</a> &bull; 
<a href="LICENSE">License</a> &bull; 
<a href="https://github.com/pratyakshm/WinRice/blob/main/doc/CONTRIBUTING.md">Contribution</a>
</p>

## About

WinRice is a PowerShell script designed to automate setting up a new Windows device. It automates a few of the useful things that people generally do in a fresh Windows installation or a new Windows device.

## Core Features

- Batch installs apps and features automatically
- Configures Windows UI
- Configures Windows Update policies
- Enhances privacy
- Disables non-essential tasks
- Disables silent installation of apps from Microsoft Store
- Disables suggestions and tips
- Exposes hidden power options
- Hardens security
- Removes non-essential apps
- Removes non-essential features

## Pre-requisites

- You've read the documentation. If you're running WinRice for the first time, take a look at [`Main-brief.md`](https://github.com/pratyakshm/WinRice/blob/main/doc/Main-brief.md). The directory that contains all documents is available [here](https://github.com/pratyakshm/WinRice/tree/main/doc).
- Your device must:
  - Be connected to the Internet.
  - Be powered by an [in-service Windows version](https://github.com/pratyakshm/WinRice/blob/main/doc/Supported-winver.md).
  - Not have any pending restarts.
  - Be up to date. \*

\* If you've just installed Windows, please ensure that all updates from Microsoft Store and Windows Update are installed. This is because WinRice uses some components that are only available in the latest updates. This is to ensure that WinRice works seamlessly on your device.

## Download

<a href="https://github.com/pratyakshm/WinRice/releases/download/v0.5.04112021/WinRice.exe"><img alt="Download Now" src="https://user-images.githubusercontent.com/54220235/216923215-0d0ecd81-8d99-47bb-828c-55aa894d3c6a.png"></a>

<!-- #### Alternative method
  <details><summary> Click to expand </summary>
  Alternatively, use Win + X shortcut to open the quick links menu, and from there open Terminal (Admin) (or Windows PowerShell (Admin) if you are on Windows 10) and execute this command:

```powershell
Invoke-WebRequest bit.ly/WinRice | Invoke-Expression
```
  </details>
-->
