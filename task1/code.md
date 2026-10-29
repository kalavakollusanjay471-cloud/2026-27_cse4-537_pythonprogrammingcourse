# University Scholarship Allocation System using Python

## 1. Problem Statement

The University Scholarship Allocation System is designed to identify eligible students and rank them for scholarship allocation based on academic performance and financial background.

The system evaluates each student using the following criteria:

1. Aggregate marks: Minimum 75%.
2. Subject-wise marks: At least 40 marks in every subject.
3. Attendance: Minimum 75%.
4. Family annual income: Not more than ₹2,50,000.
5. Ranking: Eligible students are ranked by aggregate marks in descending order.
6. Tie-breaking rules: If aggregate marks are equal, higher attendance gets priority. If attendance is also equal, lower family income gets priority. If all three are equal, the student whose name comes first alphabetically gets priority.

The system displays each student's eligibility status and produces a ranked list of eligible applicants.

Note: These thresholds and tie-breaking rules are example rules for this program. A university can replace them with its official scholarship policy.

## 2. Algorithm

1. Start the program.
2. Read the number of students.
3. For each student, enter their name, aggregate percentage, subject marks, attendance percentage, and annual family income.
4. Check whether the aggregate percentage is at least 75%.
5. Check whether every subject mark is at least 40.
6. Check whether attendance is at least 75%.
7. Check whether annual family income is at most ₹2,50,000.
8. If all conditions are satisfied, mark the student as eligible; otherwise, mark them as not eligible.
9. Sort eligible students by:
   - Higher aggregate percentage first.
   - Higher attendance first.
   - Lower annual family income first.
   - Alphabetical order of name.
10. Display eligibility results and the final scholarship ranking.
11. Stop.

## 3. Flowchart


```
  Enter number of students: 3

Enter details for Student 1
Student name: Ravi
Aggregate percentage: 90
Enter marks in 3 subjects: 80 85 90
Attendance percentage: 90
Annual family income (Rs.): 200000

Enter details for Student 2
Student name: Priya
Aggregate percentage: 90
Enter marks in 3 subjects: 85 90 88
Attendance percentage: 95
Annual family income (Rs.): 220000

Enter details for Student 3
Student name: Kiran
Aggregate percentage: 82
Enter marks in 3 subjects: 70 35 80
Attendance percentage: 85
Annual family income (Rs.): 150000      
```

## 5. Sample Input

```
Enter number of students: 3

Enter details for Student 1
Student name: Ravi
Aggregate percentage: 90
Enter marks in 3 subjects: 80 85 90
Attendance percentage: 90
Annual family income (Rs.): 200000

Enter details for Student 2
Student name: Priya
Aggregate percentage: 90
Enter marks in 3 subjects: 85 90 88
Attendance percentage: 95
Annual family income (Rs.): 220000

Enter details for Student 3
Student name: Kiran
Aggregate percentage: 82
Enter marks in 3 subjects: 70 35 80
Attendance percentage: 85
Annual family income (Rs.): 150000
```

## 6. Sample Output

```
--- Eligibility Results ---
Ravi: Eligible
Priya: Eligible
Kiran: Not Eligible

--- Scholarship Ranking ---
1. Priya | Aggregate: 90.00% | Attendance: 95.00% | Income: Rs.220000
2. Ravi | Aggregate: 90.00% | Attendance: 90.00% | Income: Rs.200000
```

Output explanation:

- Priya ranks first because her aggregate marks equal Ravi's, but her attendance is higher.
- Ravi ranks second because his attendance is lower than Priya's.
- Kiran is not eligible because one subject mark is 35, below the minimum of 40.

## 7. Mermaid Flowchart Code

You can paste this code into the [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate a flowchart diagram.

\#chatgpt-mermaid-\_r_c3\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_c3\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_c3\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_c3\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_c3\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_c3\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_c3\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_c3\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_c3\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_c3\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_c3\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_c3\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_c3\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_c3\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_c3\_ p{margin:0;}#chatgpt-mermaid-\_r_c3\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_c3\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_c3\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_c3\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_c3\_ .label text,#chatgpt-mermaid-\_r_c3\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_c3\_ .node rect,#chatgpt-mermaid-\_r_c3\_ .node circle,#chatgpt-mermaid-\_r_c3\_ .node ellipse,#chatgpt-mermaid-\_r_c3\_ .node polygon,#chatgpt-mermaid-\_r_c3\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_c3\_ .rough-node .label text,#chatgpt-mermaid-\_r_c3\_ .node .label text,#chatgpt-mermaid-\_r_c3\_ .image-shape .label,#chatgpt-mermaid-\_r_c3\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_c3\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_c3\_ .rough-node .label,#chatgpt-mermaid-\_r_c3\_ .node .label,#chatgpt-mermaid-\_r_c3\_ .image-shape .label,#chatgpt-mermaid-\_r_c3\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_c3\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_c3\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_c3\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_c3\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_c3\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_c3\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_c3\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_c3\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_c3\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_c3\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_c3\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_c3\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_c3\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_c3\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_c3\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_c3\_ .icon-shape,#chatgpt-mermaid-\_r_c3\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_c3\_ .icon-shape p,#chatgpt-mermaid-\_r_c3\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_c3\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_c3\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_c3\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_c3\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_c3\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_c3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_c3\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_c3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_c3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_c3\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_c3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_c3\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_c3\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_c3\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_c3\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_c3\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_c3\_ .node rect,#chatgpt-mermaid-\_r_c3\_ .node circle,#chatgpt-mermaid-\_r_c3\_ .node ellipse,#chatgpt-mermaid-\_r_c3\_ .node polygon,#chatgpt-mermaid-\_r_c3\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_c3\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_c3\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_c3\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_c3\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_c3\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}#chatgpt-mermaid-\_r_c3\_ .startEnd rect{fill:rgb(217, 234, 211)!important;stroke:rgb(56, 118, 29)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .startEnd polygon{fill:rgb(217, 234, 211)!important;stroke:rgb(56, 118, 29)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .startEnd ellipse{fill:rgb(217, 234, 211)!important;stroke:rgb(56, 118, 29)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .startEnd circle{fill:rgb(217, 234, 211)!important;stroke:rgb(56, 118, 29)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .startEnd path{fill:rgb(217, 234, 211)!important;stroke:rgb(56, 118, 29)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .startEnd tspan{fill:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .process rect{fill:rgb(217, 234, 247)!important;stroke:rgb(17, 85, 204)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .process polygon{fill:rgb(217, 234, 247)!important;stroke:rgb(17, 85, 204)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .process ellipse{fill:rgb(217, 234, 247)!important;stroke:rgb(17, 85, 204)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .process circle{fill:rgb(217, 234, 247)!important;stroke:rgb(17, 85, 204)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .process path{fill:rgb(217, 234, 247)!important;stroke:rgb(17, 85, 204)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .process tspan{fill:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .decision rect{fill:rgb(255, 242, 204)!important;stroke:rgb(191, 144, 0)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .decision polygon{fill:rgb(255, 242, 204)!important;stroke:rgb(191, 144, 0)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .decision ellipse{fill:rgb(255, 242, 204)!important;stroke:rgb(191, 144, 0)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .decision circle{fill:rgb(255, 242, 204)!important;stroke:rgb(191, 144, 0)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .decision path{fill:rgb(255, 242, 204)!important;stroke:rgb(191, 144, 0)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-\_r_c3\_ .decision tspan{fill:rgb(0, 0, 0)!important;}StartInput number of studentsEnter name, aggregate marks,subject marks, attendance andincomeAggregate = 75%?Mark Not EligibleEvery subject = 40?Attendance = 75%?Income <= Rs. 250000?Mark EligibleMore students?Collect eligible studentsSort by aggregate descendingBreak ties by attendance,income and nameDisplay eligibility and rankingStopNoYesNoYesNoYesNoYesYesNo

## 8. Conclusion

The University Scholarship Allocation System automates student eligibility checking, reduces manual errors, and ranks eligible students fairly using predefined criteria and tie-breaking rules. It can be extended to support more subjects, different scholarship categories, and a fixed number of available scholarships.
