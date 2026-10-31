# Campus Event Financial Planning – Python Program

## 1. Problem Statement

Develop a Python program to manage the financial planning of a campus event. The program calculates the total event expenses, including venue, equipment, catering, transport, and certificate costs.

The program should:

1. Accept the cost of venue, equipment, catering, transport, and certificates.
2. Calculate the total event expenditure.
3. Accept the expected number of participants.
4. Calculate the contribution required from each participant.
5. Calculate the available sponsorship amount.
6. Determine the sponsorship shortfall, if any.
7. Calculate the minimum number of registrations required to break even.
8. Display the complete event financial report.

## 2. Algorithm

1. Start the program.
2. Input the venue cost.
3. Input the equipment cost.
4. Input the catering cost.
5. Input the transport cost.
6. Input the certificate cost per participant.
7. Input the expected number of participants.
8. Input the available sponsorship amount.
9. Calculate the fixed expenses.

`Fixed Cost = Venue + Equipment + Transport`

10\. Calculate the variable expenses.

`Variable Cost = (Catering + Certificate Cost) × Participants`

11\. Calculate total event cost.

`Total Cost = Fixed Cost + Variable Cost`

12\. Calculate the amount remaining after sponsorship.

`Required Amount = Total Cost - Sponsorship`

13\. Calculate participant contribution.

`Contribution = Required Amount / Participants`

14. Calculate the minimum registration count needed to break even using the participant contribution and variable cost per participant.
15. Display all expenses, contributions, sponsorship shortfall, and break-even registrations.
16. Stop the program.

## 3. Flowchart


```

flowchart TD
    A([Start]) --> B[/Enter venue cost/]
    B --> C[/Enter equipment and transport costs/]
    C --> D[/Enter catering and certificate costs per participant/]
    D --> E[/Enter participants and sponsorship/]
    E --> F{Are inputs valid?}
    F -- No --> G[Display Invalid Input]
    G --> Z([Stop])
    F -- Yes --> H[Calculate fixed cost]
    H --> I[Calculate variable cost]
    I --> J[Calculate total event cost]
    J --> K[Calculate sponsorship shortfall]
    K --> L[Calculate participant contribution]
    L --> M[Calculate minimum break-even registrations]
    M --> N[Display financial report]
    N --> Z

```

## 5. Sample Input

```
===== CAMPUS EVENT FINANCIAL PLANNING =====

Enter venue cost: 20000
Enter equipment cost: 10000
Enter transport cost: 5000
Enter catering cost per participant: 200
Enter certificate cost per participant: 50
Enter expected number of participants: 100
Enter available sponsorship amount: 15000
```

## 6. Sample Output

```
===== EVENT FINANCIAL REPORT =====

Venue Cost: 20000.0
Equipment Cost: 10000.0
Transport Cost: 5000.0
Catering Cost: 20000.0
Certificate Cost: 5000.0

--------------------------------
Fixed Cost: 35000.0
Variable Cost: 25000.0
Total Event Cost: 60000.0

Sponsorship Amount: 15000.0
Sponsorship Shortfall: 45000.0

Participant Contribution: 450.0

Minimum Registrations to Break Even: 175

===== EVENT PLANNING COMPLETED =====
```

## 7. Mermaid Flowchart Code

\#chatgpt-mermaid-\_r_dr\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_dr\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_dr\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_dr\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_dr\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dr\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_dr\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_dr\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_dr\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_dr\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_dr\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_dr\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dr\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dr\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_dr\_ p{margin:0;}#chatgpt-mermaid-\_r_dr\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dr\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dr\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dr\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_dr\_ .label text,#chatgpt-mermaid-\_r_dr\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dr\_ .node rect,#chatgpt-mermaid-\_r_dr\_ .node circle,#chatgpt-mermaid-\_r_dr\_ .node ellipse,#chatgpt-mermaid-\_r_dr\_ .node polygon,#chatgpt-mermaid-\_r_dr\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_dr\_ .rough-node .label text,#chatgpt-mermaid-\_r_dr\_ .node .label text,#chatgpt-mermaid-\_r_dr\_ .image-shape .label,#chatgpt-mermaid-\_r_dr\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_dr\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_dr\_ .rough-node .label,#chatgpt-mermaid-\_r_dr\_ .node .label,#chatgpt-mermaid-\_r_dr\_ .image-shape .label,#chatgpt-mermaid-\_r_dr\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_dr\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_dr\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dr\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dr\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_dr\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_dr\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_dr\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dr\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dr\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_dr\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_dr\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dr\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dr\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_dr\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dr\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_dr\_ .icon-shape,#chatgpt-mermaid-\_r_dr\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_dr\_ .icon-shape p,#chatgpt-mermaid-\_r_dr\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_dr\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_dr\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dr\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_dr\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_dr\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_dr\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_dr\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_dr\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_dr\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dr\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_dr\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dr\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_dr\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_dr\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_dr\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_dr\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_dr\_ .node rect,#chatgpt-mermaid-\_r_dr\_ .node circle,#chatgpt-mermaid-\_r_dr\_ .node ellipse,#chatgpt-mermaid-\_r_dr\_ .node polygon,#chatgpt-mermaid-\_r_dr\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_dr\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_dr\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_dr\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_dr\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dr\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter venue costEnter equipment and transportcostsEnter catering and certificatecosts per participantEnter participants andsponsorshipAre inputs valid?Display Invalid InputStopCalculate fixed costCalculate variable costCalculate total event costCalculate sponsorship shortfallCalculate participantcontributionCalculate minimum break-evenregistrationsDisplay financial reportNoYes

## 8. Important Formulas

| Calculation              | Formula                                                                 |
| ------------------------ | ----------------------------------------------------------------------- |
| Fixed Cost               | Venue + Equipment + Transport                                           |
| Variable Cost            | Participants × (Catering + Certificate)                                 |
| Total Cost               | Fixed Cost + Variable Cost                                              |
| Sponsorship Shortfall    | Max(0, Total Cost − Sponsorship)                                        |
| Participant Contribution | Shortfall ÷ Participants                                                |
| Break-even Registrations | Fixed Cost ÷ (Contribution − Variable Cost per participant), rounded up |

Note: The break-even registration count assumes the calculated participant contribution remains unchanged as registrations increase, while catering and certificate costs vary with the number of participants.

Revenue

Total cost

Loss

Profit

10203040506050010001500Quantity$Q\*

\\(Q^\*=\frac{F}{p-v}=\frac{\text{600}}{\text{35}-\text{15}}=\text{30}\\)

Q\* is the break-even quantity where total revenue matches total cost.

\\(F\\)

$

\\(v\\)

$/unit

\\(p\\)

$/unit

Give feedback

## 9. Expected Result

- Calculates all campus event expenses.
- Determines the total event budget.
- Calculates individual participant contributions.
- Identifies the sponsorship shortfall.
- Finds the minimum registrations required to break even.
- Generates a complete financial report for the campus event.
