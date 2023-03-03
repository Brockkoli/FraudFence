# FraudFence
## Web Security

Web analysis tool 

- Whois
  - Title
  - Description
  - Registrar
  - Creation date
  - Expiration date
  - Name servers
  - Registrant name, email, address
- DNS Lookup
  - A record
  - AAAA record
  - ANY record
  - CAA record
  - CNAME record
  - MX record
  - NS record
  - TXT record
- Port enumeration
  - Full scan: 1 to 65535
  - Default: 1000 most popular port number
  - Custom range: 1-500 for eg

- Security rating/risk
  - uses a pre-trained AI learning machine model as well as a database of blacklisted websites to protect non-tech savvy users against phishing attacks. We chose to develop a solution that is easy to use for the non-technical savvy such as children, and the elderly. The solution will ensure that they are cognizant of such malicious intents, especially in an ever-growing world of technology.
    - WOT Web Risk and Safe browsing
      - Display reputations, categories, and third-party blacklist information. Each target result contains the following:

        - The response object has one attribute for each target, named by the unchanged target name given in the host’s parameter.

        - Each target object has a target attribute, which contains the normalized target name.

        - Safety and ChildSafety attributes which consist of:

            - Status - One of the predefined strings representing if the target is generally safe/safe (Currently not supported for ChildSafety). Possible values are: SAFE, NOT_SAFE, UNKNOWN, SUSPICIOUS
            - Reputation - integer between 0-100. The target’s reputation score for safety/child safety.
            - Confidence - integer between 0-100. The confidence WOT’s algorithm attributes to the above score.
            - Each target object also may have a categories array, which contains one or more category identifier attributes, the category friendly name, and their confidence values.
            ![raw html display](https://user-images.githubusercontent.com/59412437/222772375-6d004d2d-87ff-46b3-9a1f-8b653f17f72d.png)

