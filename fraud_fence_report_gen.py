# Importing modules
from dnslookup import dnslookup
from headers import headers
#from info import whois_check
from locationchecker import serverlocationchecker
from portscan import portscan_check
from sslinformation import ssl_checker

html = """

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.104.2">
    <title>FraudFence Report</title>



    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

  <style>
    .table-of-contents{
      font-size: 25px;
      font-weight: bold;
    }
    .nav-link{
      font-size: 20px;
    }
    h2 {
      padding-top: 20px;
      padding-bottom: 10px;
      font-weight: bold;
    }
      .nav-pills .nav-link:hover {
        background-color: rgba(0, 0, 0, .075);
      }
    </style>

  </head>
  <body>

  <main class="d-flex flex-nowrap">
    <div class="d-flex flex-column flex-shrink-0 p-3 bg-light" style="width: 280px; min-height: 100vh;position: fixed;">
      <a class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
        <svg class="bi pe-none me-2" width="21" height="32"><use xlink:href="#bootstrap"/></svg>
        <span class="table-of-contents">Table of Contents</span>
      </a>
      <hr>
      <ul class="nav nav-pills flex-column mb-auto">
        <li class="nav-item">
          <a href="#Who Is" class="nav-link link-dark" aria-current="page">
            <svg class="bi pe-none me-2" width="16" height="16"></svg>
            Who Is
          </a>
        </li>
        <li>
          <a href="#Port Scan" class="nav-link link-dark">
            <svg class="bi pe-none me-2" width="16" height="16"></svg>
            Port Scan
          </a>
        </li>
        <li>
          <a href="#DNS Lookup" class="nav-link link-dark">
            <svg class="bi pe-none me-2" width="16" height="16"></svg>
            DNS Lookup
          </a>
        </li>
        <li>
          <a href="#Server Location" class="nav-link link-dark">
            <svg class="bi pe-none me-2" width="16" height="16"></svg>
            Server Location
          </a>
        </li>
        <li>
          <a href="#Web Headers" class="nav-link link-dark">
            <svg class="bi pe-none me-2" width="16" height="16"></svg>
            Web Headers
          </a>
        </li>
        <li>
          <a href="#SSL Information" class="nav-link link-dark">
            <svg class="bi pe-none me-2" width="16" height="16"></svg>
            SSL Information
          </a>
        </li>
      </ul>
      <hr>
    </div>
    <!-- Main Content -->
    <div class="container">
      <div class="row">
      
        <!-- Section 1 -->
        <div class="col-12">
          <section id="Who Is">
            <h2>Who Is</h2>
            <div class="card">
              <div class="card-body">
                <!-- add content here -->
              </div>
            </div>
          </section>
        </div>
        
        <!-- Section 2 -->
        <div class="col-12">
          <section id="Port Scan">
            <h2>Port Scan</h2>
            <div class="card">
              <div class="card-body">
                <!-- add content here -->
              </div>
            </div>
          </section>
        </div>
        
        <!-- Section 3 -->
        <div class="col-12">
          <section id="DNS Lookup">
            <h2>DNS Lookup</h2>
            <div class="card">
              <div class="card-body">
                <!-- add content here -->
              </div>
            </div>
          </section>
        </div>
        
        <!-- Section 4 -->
        <div class="col-12">
          <section id="Server Location">
            <h2>Server Location</h2>
            <div class="card">
              <div class="card-body">
                <!-- add content here -->
              </div>
            </div>
          </section>
        </div>
        
        <!-- Section 5 -->
        <div class="col-12">
          <section id="Web Headers">
            <h2>Web Headers</h2>
            <div class="card">
              <div class="card-body">
                <!-- add content here -->                
              </div>
            </div>
          </section>
        </div>

        <!-- Section 6 -->
        <div class="col-lg-12">
          <section id="SSL Information">
            <h2>SSL Information</h2>
            <div class="card">
              <div class="card-body">
                <!-- add content here -->
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  
    
  </main>
  

  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

  </body>
</html>
"""
with open('FraudFence_report.html', "w") as f:
    f.write(html)