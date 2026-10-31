# Attendance Recovery Computation – Python Program

## 1. Problem Statement

Develop a Python program to calculate a student's current attendance percentage and determine the minimum number of consecutive classes the student must attend to reach a required eligibility percentage.

The program should:

1. Accept the student's name.
2. Accept the total number of classes conducted.
3. Accept the number of classes attended.
4. Calculate the current attendance percentage.
5. Accept the required eligibility attendance percentage.
6. Calculate the minimum consecutive classes required to reach the eligibility threshold.
7. Analyze different future attendance scenarios, such as attending all upcoming classes or missing some classes.
8. Display the final attendance recovery report.

## 2. Algorithm

1. Start the program.
2. Enter the student's name.
3. Enter total classes conducted.
4. Enter classes attended.
5. Enter the required attendance percentage.
6. Validate the entered values.
7. Calculate current attendance percentage.

`Current Attendance = (Classes Attended / Total Classes) × 100`

8. Check whether the student already meets the eligibility threshold.
9. If not eligible:
   - Assume the student attends all upcoming classes.
   - Calculate the minimum consecutive classes required to reach the threshold.
10. Calculate attendance under different future scenarios.
11. Display current attendance percentage.
12. Display the minimum required classes and future scenario results.
13. Stop the program.

## 3. Flowchart



```

flowchart TD
    A([Start]) --> B[/Enter student name/]
    B --> C[/Enter total classes and attended classes/]
    C --> D[/Enter eligibility percentage/]
    D --> E{Are inputs valid?}
    E -- No --> F[Display Invalid Input]
    F --> Z([Stop])
    E -- Yes --> G[Calculate current attendance]
    G --> H{Attendance >= Eligibility?}
    H -- Yes --> I[Display Eligible]
    I --> J[Required Classes = 0]
    H -- No --> K[Calculate minimum consecutive classes]
    J --> L[/Enter upcoming classes/]
    K --> L
    L --> M[Calculate future attendance scenarios]
    M --> N[Calculate final attendance percentages]
    N --> O[Check eligibility for each scenario]
    O --> P[Display attendance recovery report]
    P --> Z

```

## 5. Sample Input

```
===== ATTENDANCE RECOVERY SYSTEM =====

Enter student name: Sanjay
Enter total classes conducted: 100
Enter classes attended: 65
Enter required attendance percentage: 75

Enter number of upcoming classes: 40
```

## 6. Sample Output

```
===== CURRENT ATTENDANCE =====

Student Name: Sanjay
Total Classes: 100
Attended Classes: 65
Current Attendance: 65.0 %
Eligibility Requirement: 75.0 %

Status: NOT ELIGIBLE

Minimum consecutive classes to attend: 40

===== FUTURE ATTENDANCE SCENARIOS =====

Attend all classes
Classes Attended: 40
Final Attendance: 75.0 %
Status: ELIGIBLE

Attend 75% classes
Classes Attended: 30
Final Attendance: 71.43 %
Status: NOT ELIGIBLE

Attend 50% classes
Classes Attended: 20
Final Attendance: 67.86 %
Status: NOT ELIGIBLE

Attend no classes
Classes Attended: 0
Final Attendance: 46.43 %
Status: NOT ELIGIBLE

===== ATTENDANCE REPORT COMPLETED =====
```

## 7. Mermaid Flowchart Code

\#chatgpt-mermaid-\_r_ih\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_ih\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ih\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ih\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_ih\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ih\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_ih\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_ih\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_ih\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_ih\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_ih\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_ih\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ih\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ih\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_ih\_ p{margin:0;}#chatgpt-mermaid-\_r_ih\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ih\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ih\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ih\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_ih\_ .label text,#chatgpt-mermaid-\_r_ih\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ih\_ .node rect,#chatgpt-mermaid-\_r_ih\_ .node circle,#chatgpt-mermaid-\_r_ih\_ .node ellipse,#chatgpt-mermaid-\_r_ih\_ .node polygon,#chatgpt-mermaid-\_r_ih\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_ih\_ .rough-node .label text,#chatgpt-mermaid-\_r_ih\_ .node .label text,#chatgpt-mermaid-\_r_ih\_ .image-shape .label,#chatgpt-mermaid-\_r_ih\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_ih\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_ih\_ .rough-node .label,#chatgpt-mermaid-\_r_ih\_ .node .label,#chatgpt-mermaid-\_r_ih\_ .image-shape .label,#chatgpt-mermaid-\_r_ih\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_ih\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_ih\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ih\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ih\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_ih\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_ih\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_ih\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_ih\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_ih\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_ih\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_ih\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ih\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ih\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_ih\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ih\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_ih\_ .icon-shape,#chatgpt-mermaid-\_r_ih\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_ih\_ .icon-shape p,#chatgpt-mermaid-\_r_ih\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_ih\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_ih\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_ih\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_ih\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_ih\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_ih\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_ih\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_ih\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_ih\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ih\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_ih\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ih\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_ih\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_ih\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_ih\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_ih\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_ih\_ .node rect,#chatgpt-mermaid-\_r_ih\_ .node circle,#chatgpt-mermaid-\_r_ih\_ .node ellipse,#chatgpt-mermaid-\_r_ih\_ .node polygon,#chatgpt-mermaid-\_r_ih\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_ih\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_ih\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_ih\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_ih\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ih\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter student nameEnter total classes andattended classesEnter eligibility percentageAre inputs valid?Display Invalid InputStopCalculate current attendanceAttendance = Eligibility?Display EligibleRequired Classes = 0Calculate minimumconsecutive classesEnter upcoming classesCalculate future attendancescenariosCalculate final attendancepercentagesCheck eligibility for eachscenarioDisplay attendance recoveryreportNoYesYesNo

## 8. Important Formulas

1\. Current Attendance Percentage

\\[ \text{Attendance} = \frac{\text{Attended Classes}}{\text{Total Classes}} \times 100 \\]

2\. Minimum Consecutive Classes Required

\\[ \frac{A+x}{T+x}\times100\geq E \\]

Where:

- A = Classes attended
- T = Total classes conducted
- x = Additional consecutive classes to attend
- E = Required eligibility percentage

Rearranging:

\\[ x=\left\lceil\frac{ET-100A}{100-E}\right\rceil \\]

3\. Future Attendance Percentage

\\[ \text{Future Attendance} = \frac{\text{Previous Attended + Future Attended}} {\text{Previous Total + Future Total}}\times100 \\]

## 9. Expected Result

- Calculates current attendance percentage.
- Checks minimum attendance eligibility.
- Determines the minimum consecutive classes required.
- Compares different future attendance scenarios.
- Displays final eligibility status.

Note: The program assumes that all future classes are conducted and that attending a class increases both attended and total classes by one. The 75% and 50% scenarios use whole-number attendance counts rounded down.
