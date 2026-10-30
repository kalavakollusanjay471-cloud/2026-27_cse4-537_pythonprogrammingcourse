# Hospital Billing and Patient Classification System

## 1. Problem Statement

Develop a Python program for a Hospital Billing and Patient Classification System.

The system calculates the total hospital bill based on consultation charges, diagnostic charges, and treatment charges. It applies conditional concessions according to patient category and validates billing constraints.

The program classifies patients according to the supplied payment policy:

- General Patient: No concession.
- Senior Citizen: 10% concession.
- BPL Patient: 20% concession.
- Emergency Patient: 5% concession.

The program displays the total bill, concession amount, final payable amount, and patient classification.

## 2. Algorithm

1. Start the program.
2. Read the patient name and age.
3. Read consultation charges.
4. Read diagnostic charges.
5. Read treatment charges.
6. Calculate the total bill.
7. Check whether the entered charges are valid (not negative).
8. Identify the patient category.
9. Apply the appropriate concession percentage.
10. Calculate the concession amount.
11. Calculate the final payable amount.
12. Display the billing details and patient classification.
13. Stop the program.

## 3. Flowchart




```
===== HOSPITAL BILLING SYSTEM =====
Enter patient name: Sanjay
Enter patient age: 65
Enter consultation charges: 500
Enter diagnostic charges: 1000
Enter treatment charges: 5000

Select Patient Category:
1. General Patient
2. Senior Citizen
3. BPL Patient
4. Emergency Patient

Enter your choice (1-4): 2
```

## 5. Sample Input

```
===== HOSPITAL BILLING SYSTEM =====
Enter patient name: Sanjay
Enter patient age: 65
Enter consultation charges: 500
Enter diagnostic charges: 1000
Enter treatment charges: 5000

Select Patient Category:
1. General Patient
2. Senior Citizen
3. BPL Patient
4. Emergency Patient

Enter your choice (1-4): 2
```

## 6. Sample Output

```
===== FINAL HOSPITAL BILL =====

Patient Name: Sanjay
Patient Age: 65
Patient Category: Senior Citizen

Consultation Charges: Rs. 500.0
Diagnostic Charges: Rs. 1000.0
Treatment Charges: Rs. 5000.0

Total Bill: Rs. 6500.0
Concession: 10 %

Concession Amount: Rs. 650.0
Final Payable Amount: Rs. 5850.0
```

## 7. Mermaid Flowchart Code

You can copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_ea\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_ea\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ea\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ea\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_ea\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ea\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_ea\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_ea\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_ea\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_ea\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_ea\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_ea\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ea\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ea\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_ea\_ p{margin:0;}#chatgpt-mermaid-\_r_ea\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ea\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ea\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ea\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_ea\_ .label text,#chatgpt-mermaid-\_r_ea\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ea\_ .node rect,#chatgpt-mermaid-\_r_ea\_ .node circle,#chatgpt-mermaid-\_r_ea\_ .node ellipse,#chatgpt-mermaid-\_r_ea\_ .node polygon,#chatgpt-mermaid-\_r_ea\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_ea\_ .rough-node .label text,#chatgpt-mermaid-\_r_ea\_ .node .label text,#chatgpt-mermaid-\_r_ea\_ .image-shape .label,#chatgpt-mermaid-\_r_ea\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_ea\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_ea\_ .rough-node .label,#chatgpt-mermaid-\_r_ea\_ .node .label,#chatgpt-mermaid-\_r_ea\_ .image-shape .label,#chatgpt-mermaid-\_r_ea\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_ea\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_ea\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ea\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ea\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_ea\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_ea\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_ea\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_ea\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_ea\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_ea\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_ea\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ea\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ea\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_ea\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_ea\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_ea\_ .icon-shape,#chatgpt-mermaid-\_r_ea\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_ea\_ .icon-shape p,#chatgpt-mermaid-\_r_ea\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_ea\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_ea\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_ea\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_ea\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_ea\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_ea\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_ea\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_ea\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_ea\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ea\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_ea\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ea\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_ea\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_ea\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_ea\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_ea\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_ea\_ .node rect,#chatgpt-mermaid-\_r_ea\_ .node circle,#chatgpt-mermaid-\_r_ea\_ .node ellipse,#chatgpt-mermaid-\_r_ea\_ .node polygon,#chatgpt-mermaid-\_r_ea\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_ea\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_ea\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_ea\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_ea\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_ea\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter Patient Name and AgeEnter Consultation ChargesEnter Diagnostic ChargesEnter Treatment ChargesAre Age and Charges Valid?Display Invalid InputStopCalculate Total BillSelect Patient CategoryPatient CategoryDiscount = 0%Discount = 10%Discount = 20%Discount = 5%Display Invalid CategoryCalculate ConcessionCalculate Final Payable AmountDisplay Hospital BillNoYesGeneralSenior CitizenBPLEmergencyInvalid

## 8. Result

The Hospital Billing and Patient Classification System was successfully implemented using Python. It calculates hospital charges, validates inputs, applies conditional concessions, and displays the final payable amount based on patient classification.

Note: The concession percentages and categories used here are example policies for this program. Actual hospital payment policies may differ.
