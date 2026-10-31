# Railway Fare and Reservation Calculator

## 1. Problem Statement

Develop a Python program to calculate railway ticket fares for multiple passengers based on the following conditions:

1. Calculate ticket fare according to the travelling distance.
2. Provide different travel classes such as Sleeper, AC 3-Tier, and AC 2-Tier.
3. Apply age-based concessions for children and senior citizens.
4. Add reservation charges based on the selected class.
5. Calculate the total ticket amount for all passengers.
6. Calculate cancellation penalties when a ticket is cancelled.
7. Display a detailed and formatted railway reservation bill.

## 2. Algorithm

1. Start the program.
2. Enter the number of passengers.
3. Enter the travelling distance in kilometres.
4. Select the travel class.
5. Enter the age of each passenger.
6. Calculate the basic fare based on distance and class.
7. Apply age-based concessions:
   - Below 5 years: Free ticket.
   - 5 to 11 years: 50% concession.
   - 60 years and above: 40% concession.
   - Others: No concession.
8. Add reservation charges.
9. Calculate the total fare for each passenger.
10. Ask whether the ticket is cancelled.
11. If cancelled, calculate the cancellation penalty.
12. Display the final railway bill.
13. Stop the program.

## 3. Flowchart


```
 
flowchart TD
    A([Start]) --> B[/Enter journey distance/]
    B --> C[/Enter number of passengers/]
    C --> D[/Select travel class/]
    D --> E[Calculate fare rate and reservation fee]
    E --> F[Set total fare = 0]
    F --> G[/Enter passenger name and age/]
    G --> H[Calculate basic fare]
    H --> I{Check passenger age}
    I -->|Below 5| J[100% concession]
    I -->|5 to 11| K[50% concession]
    I -->|12 to 59| L[No concession]
    I -->|60 and above| M[40% concession]
    J --> N[Calculate ticket fare]
    K --> N
    L --> N
    M --> N
    N --> O[Add reservation fee if applicable]
    O --> P[Add fare to total]
    P --> Q{More passengers?}
    Q -->|Yes| G
    Q -->|No| R[Display total fare]
    R --> S{Cancel tickets?}
    S -->|Yes| T[Calculate cancellation penalty]
    T --> U[Calculate refund amount]
    S -->|No| V[Display reservation confirmation]
    U --> W[Display final bill]
    V --> W
    W --> X([Stop])
   
```

## 5. Sample Input

```
===== RAILWAY FARE CALCULATOR =====

Enter journey distance (km): 200
Enter number of passengers: 3

Select Travel Class:
1. Sleeper
2. AC 3-Tier
3. AC 2-Tier

Enter your choice: 1

Passenger 1
Enter passenger name: Sanjay
Enter passenger age: 20

Passenger 2
Enter passenger name: Ravi
Enter passenger age: 65

Passenger 3
Enter passenger name: Kumar
Enter passenger age: 10

Do you want to cancel the tickets? (yes/no): no
```

## 6. Sample Output

```
===== RAILWAY FARE CALCULATOR =====

Passenger Name: Sanjay
Age: 20
Travel Class: Sleeper
Basic Fare: Rs. 300.0
Concession: 0 %
Reservation Fee: Rs. 20
Ticket Fare: Rs. 320.0

Passenger Name: Ravi
Age: 65
Travel Class: Sleeper
Basic Fare: Rs. 300.0
Concession: 40 %
Reservation Fee: Rs. 20
Ticket Fare: Rs. 200.0

Passenger Name: Kumar
Age: 10
Travel Class: Sleeper
Basic Fare: Rs. 300.0
Concession: 50 %
Reservation Fee: Rs. 20
Ticket Fare: Rs. 170.0

===== RESERVATION SUMMARY =====

Total Passengers: 3
Total Ticket Fare: Rs. 690.0

Tickets successfully reserved!

Thank you for using Railway Reservation System!
```

## 7. Mermaid Flowchart Code

You can copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_gn\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_gn\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_gn\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_gn\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_gn\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gn\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_gn\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_gn\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_gn\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_gn\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_gn\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_gn\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gn\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gn\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_gn\_ p{margin:0;}#chatgpt-mermaid-\_r_gn\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gn\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gn\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gn\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_gn\_ .label text,#chatgpt-mermaid-\_r_gn\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gn\_ .node rect,#chatgpt-mermaid-\_r_gn\_ .node circle,#chatgpt-mermaid-\_r_gn\_ .node ellipse,#chatgpt-mermaid-\_r_gn\_ .node polygon,#chatgpt-mermaid-\_r_gn\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_gn\_ .rough-node .label text,#chatgpt-mermaid-\_r_gn\_ .node .label text,#chatgpt-mermaid-\_r_gn\_ .image-shape .label,#chatgpt-mermaid-\_r_gn\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_gn\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_gn\_ .rough-node .label,#chatgpt-mermaid-\_r_gn\_ .node .label,#chatgpt-mermaid-\_r_gn\_ .image-shape .label,#chatgpt-mermaid-\_r_gn\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_gn\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_gn\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gn\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gn\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_gn\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_gn\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_gn\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gn\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gn\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_gn\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_gn\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gn\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gn\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_gn\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gn\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_gn\_ .icon-shape,#chatgpt-mermaid-\_r_gn\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_gn\_ .icon-shape p,#chatgpt-mermaid-\_r_gn\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_gn\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_gn\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gn\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_gn\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_gn\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_gn\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_gn\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_gn\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_gn\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gn\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_gn\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gn\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_gn\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_gn\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_gn\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_gn\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_gn\_ .node rect,#chatgpt-mermaid-\_r_gn\_ .node circle,#chatgpt-mermaid-\_r_gn\_ .node ellipse,#chatgpt-mermaid-\_r_gn\_ .node polygon,#chatgpt-mermaid-\_r_gn\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_gn\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_gn\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_gn\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_gn\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gn\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter journey distanceEnter number of passengersSelect travel classCalculate fare rate andreservation feeSet total fare = 0Enter passenger name and ageCalculate basic fareCheck passenger age100% concession50% concessionNo concession40% concessionCalculate ticket fareAdd reservation fee ifapplicableAdd fare to totalMore passengers?Display total fareCancel tickets?Calculate cancellation penaltyCalculate refund amountDisplay reservationconfirmationDisplay final billStopBelow 55 to 1112 to 5960 and aboveYesNoYesNo

## 8. Expected Concepts Used

| Concept      | Application                       |
| ------------ | --------------------------------- |
| Variables    | Store fare and passenger details  |
| Input/Output | Accept passenger information      |
| If-Else      | Select class and concessions      |
| For Loop     | Process multiple passengers       |
| Arithmetic   | Calculate fare and refund         |
| Operators    | Calculate discounts and penalties |

Note: The fare rates, concessions, reservation fees, and 20% cancellation penalty used here are assumed values for this educational project. They are not official Indian Railways fare or concession rules.

Project Title: Railway Fare and Reservation Calculator using Python.
