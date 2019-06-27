SOEN6611-2191AA-TEAM-H
Software Measurement Project (Summer 2019) By Team H

The aim of this project is to measure projetcs based on differnet metrics and to co-relate them. We perform differnet test coverage for developing the test cases, so the entire code is covered and there are no parts of the code left uncovered. This coverage helps us to make better test suits that can detect the anomalies and code mutants injected in the main code.

Various code coverage's or metrcis used are as follows:
Statement Coverage: is a measurement procedure wherein the number of lines of code covered is calculated based on the inputs from the users.

Branch Coverage: is a measurement procedure to calculate the number of branches executed per user input.

Mutation Score: is a testing practice wherein we check the accuracy or precision of the test cases.

Cyclomatic Complexity: is used to measure the number of linearly independent paths that can be executed in a program.

Code Churn: is used to measure the amount of change in code made to a software component over a period of time.

Post-release defect density: is used to measure the number of confirmed defects detected in a software/component during a defined period of development/operation divided by the size of the software/component.

Various Projects Used:
Apache Commons Collections:- Project-Details

Apache Commons Math:- Project-Details

Apache Commons Lang:- Project-Details

Apache Sling:- Project-Details

Apache Commons FileUpload:- Project-Details

Prerequisites and Installation Steps for EclEmma (JaCoCo)
Prerequisites: EclEmma requires Eclipse 3.8 or higher and Java or higher. It has no dependencies on a particular operating system. Eclipse Installation needs to contain the Java development tools (JDT) which is included in the default SDK installation.

Installation Steps:

Step 1. From your Eclipse menu select Help → Eclipse Marketplace.

Step 2. Search for "EclEmma".

Step 3. Hit Install for the entry "EclEmma Java Code Coverage".

Step 4. Follow the steps in the installation wizard.

Verification: The installation was successful if you can see the coverage launcher in the toolbar of the Java perspective.

Configuration for PIT Testing:
PIT requires Java 5 or above and either JUnit or TestNG to be on the classpath.

Add the plugin to build/plugins in your pom.xml

<plugin>
   <groupId>org.pitest</groupId>
   <artifactId>pitest-maven</artifactId>
   <version>1.4.8</version>
</plugin>
Mutation Coverage: It can be run directly from the commandline.
mvn org.pitest:pitest-maven:mutationCoverage
Installation and Configuration for CLOC:
Depending your operating system, one of these installation methods may work for you:
npm install -g cloc             # https://www/npmjs.com/package/cloc
sudo apt -get install cloc      # Debian, Ubuntu
sudo yum install cloc           # Red Hat, Fedora
sudo pacman -S cloc             # Arch
sudo pkg install cloc           # FreeBSD
sudo port install cloc          # Mac OS X with MacPOrts
To run cloc on Windows computers, one must first open up a command (aka DOS) window and invoke cloc.exe from the command line there.
prompt> cloc
Usage: cloc [options] <file(s)/dir(s)> | <set 1> <set 2> | <report files>
Input Options :
           --diff <set1> <set2>
           --csv  :  Write the results as comma separated values.
           --out=<file>  :  Synonym for --report-file=<file>.
Team Member Details:
 1. Ashutosh Gunjal: ashutosh.r.gunjal@gmail.com
 2. Kalpesh Thakare: kalpeshthakare1994@gmail.com
 3. Chinmay Hadadare: chinmayhadadare@gmail.com
 4. Sriparna Chakraborty: sriparna.chakraborty999@gmail.com
 5. Tapan Kumar: kumar.tapan38@gmail.com