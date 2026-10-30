# Employee Payroll and Deduction Analysis System

## 1. Problem Statement

Develop a Python program for an Employee Payroll and Deduction Analysis System.

The system calculates an employee's gross salary using basic pay, allowances, overtime, and incentives. It applies progressive deductions based on the gross salary and generates a formatted salary statement showing total earnings, deductions, and net salary.

Deduction Policy (Example):

| Gross Salary      | Deduction Rate |
| ----------------- | -------------- |
| Up to ₹20,000     | 0%             |
| ₹20,001 – ₹40,000 | 5%             |
| ₹40,001 – ₹60,000 | 10%            |
| Above ₹60,000     | 15%            |

For this example, the applicable rate is selected based on the gross salary.

## 2. Algorithm

1. Start the program.
2. Enter employee name and employee ID.
3. Enter basic salary.
4. Enter allowances.
5. Enter overtime amount.
6. Enter incentives.
7. Validate all salary amounts.
8. Calculate gross salary by adding all earnings.
9. Check the gross salary range.
10. Apply the appropriate deduction percentage.
11. Calculate deduction amount.
12. Calculate net salary.
13. Display the formatted salary statement.
14. Stop the program.

## 3. Flowchart


```
===== EMPLOYEE PAYROLL SYSTEM =====

Enter Employee Name: Sanjay
Enter Employee ID: EMP101
Enter Basic Salary: 30000
Enter Allowances: 5000
Enter Overtime Amount: 3000
Enter Incentives: 2000
```

## 5. Sample Input

```
===== EMPLOYEE PAYROLL SYSTEM =====

Enter Employee Name: Sanjay
Enter Employee ID: EMP101
Enter Basic Salary: 30000
Enter Allowances: 5000
Enter Overtime Amount: 3000
Enter Incentives: 2000
```

## 6. Sample Output

```
========== SALARY STATEMENT ==========

Employee Name: Sanjay
Employee ID: EMP101

--------------------------------------
Basic Salary       : Rs. 30000.0
Allowances         : Rs. 5000.0
Overtime Amount    : Rs. 3000.0
Incentives         : Rs. 2000.0

--------------------------------------
Gross Salary       : Rs. 40000.0
Deduction Rate     : 5 %
Total Deduction    : Rs. 2000.0

--------------------------------------
Net Salary         : Rs. 38000.0
======================================
```

## 7. Mermaid Flowchart Code

Copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_gm\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_gm\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_gm\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_gm\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_gm\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gm\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_gm\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_gm\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_gm\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_gm\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_gm\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_gm\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gm\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gm\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_gm\_ p{margin:0;}#chatgpt-mermaid-\_r_gm\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gm\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gm\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gm\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_gm\_ .label text,#chatgpt-mermaid-\_r_gm\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gm\_ .node rect,#chatgpt-mermaid-\_r_gm\_ .node circle,#chatgpt-mermaid-\_r_gm\_ .node ellipse,#chatgpt-mermaid-\_r_gm\_ .node polygon,#chatgpt-mermaid-\_r_gm\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_gm\_ .rough-node .label text,#chatgpt-mermaid-\_r_gm\_ .node .label text,#chatgpt-mermaid-\_r_gm\_ .image-shape .label,#chatgpt-mermaid-\_r_gm\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_gm\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_gm\_ .rough-node .label,#chatgpt-mermaid-\_r_gm\_ .node .label,#chatgpt-mermaid-\_r_gm\_ .image-shape .label,#chatgpt-mermaid-\_r_gm\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_gm\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_gm\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gm\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gm\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_gm\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_gm\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_gm\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gm\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gm\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_gm\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_gm\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gm\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gm\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_gm\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gm\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_gm\_ .icon-shape,#chatgpt-mermaid-\_r_gm\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_gm\_ .icon-shape p,#chatgpt-mermaid-\_r_gm\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_gm\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_gm\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gm\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_gm\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_gm\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_gm\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_gm\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_gm\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_gm\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gm\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_gm\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gm\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_gm\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_gm\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_gm\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_gm\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_gm\_ .node rect,#chatgpt-mermaid-\_r_gm\_ .node circle,#chatgpt-mermaid-\_r_gm\_ .node ellipse,#chatgpt-mermaid-\_r_gm\_ .node polygon,#chatgpt-mermaid-\_r_gm\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_gm\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_gm\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_gm\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_gm\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gm\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter Employee DetailsEnter Basic SalaryEnter AllowancesEnter Overtime and IncentivesAre All Amounts Valid?Display Invalid InputStopCalculate Gross SalaryGross Salary <= 20000?Deduction Rate = 0%Gross Salary <= 40000?Deduction Rate = 5%Gross Salary <= 60000?Deduction Rate = 10%Deduction Rate = 15%Calculate Deduction AmountCalculate Net SalaryDisplay Salary StatementNoYesYesNoYesNoYesNo

## 8. Result

The Employee Payroll and Deduction Analysis System was successfully developed using Python. It calculates gross salary, applies deductions according to salary ranges, and generates a formatted salary statement displaying the employee's net salary.

Note: The deduction rates used in this program are assumed for academic demonstration. They are not actual statutory income-tax or payroll rules.
