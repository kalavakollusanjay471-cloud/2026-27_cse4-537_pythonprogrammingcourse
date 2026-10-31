# Multi-Currency Travel Budget Analysis

## 1. Problem Statement

Develop a Python program to analyze travel expenses in multiple currencies. The program should:

1. Accept the travel budget in the home currency.
2. Accept expenses from different categories such as Food, Hotel, Transport, and Shopping.
3. Convert foreign currency expenses into the home currency using the supplied exchange rates.
4. Include currency conversion fees in the total expense.
5. Compare total planned spending with the available budget.
6. Identify and display the largest expense category.
7. Display the final travel budget report.

## 2. Algorithm

1. Start the program.
2. Read the total travel budget in home currency.
3. Read the number of expense categories.
4. For each expense, input:
   - Category name
   - Currency code
   - Expense amount
   - Exchange rate
   - Conversion fee percentage
5. Calculate the converted amount.

`Converted Amount = Expense Amount × Exchange Rate`

6\. Calculate the conversion fee.

`Conversion Fee = Converted Amount × Fee Percentage / 100`

7\. Calculate the total expense.

`Total Expense = Converted Amount + Conversion Fee`

8. Add all expenses to calculate total spending.
9. Compare total spending with the budget.
10. Identify the largest expense category.
11. Display the total spending, remaining budget or excess amount, and largest category.
12. Stop the program.

## 3. Flowchart



```

flowchart TD
    A([Start]) --> B[/Enter home currency and budget/]
    B --> C[/Enter number of expense categories/]
    C --> D[Initialize total spending = 0]
    D --> E[/Enter category, currency, amount, rate and fee/]
    E --> F[Calculate converted amount]
    F --> G[Calculate conversion fee]
    G --> H[Calculate total expense]
    H --> I[Add expense to category and total spending]
    I --> J{More expenses?}
    J -- Yes --> E
    J -- No --> K[Find largest expense category]
    K --> L{Total spending > Budget?}
    L -- Yes --> M[Calculate excess amount]
    L -- No --> N[Calculate remaining budget]
    M --> O[Display final travel report]
    N --> O
    O --> P([Stop])

```

## 5. Sample Input

```
Enter home currency (e.g. INR): INR
Enter total travel budget: 100000
Enter number of expense categories: 4

Expense 1
Enter expense category: Hotel
Enter currency code: USD
Enter expense amount: 300
Enter exchange rate: 85
Enter conversion fee percentage: 2

Expense 2
Enter expense category: Food
Enter currency code: EUR
Enter expense amount: 100
Enter exchange rate: 90
Enter conversion fee percentage: 1

Expense 3
Enter expense category: Transport
Enter currency code: USD
Enter expense amount: 150
Enter exchange rate: 85
Enter conversion fee percentage: 2

Expense 4
Enter expense category: Shopping
Enter currency code: EUR
Enter expense amount: 200
Enter exchange rate: 90
Enter conversion fee percentage: 1
```

## 6. Sample Output

```
===== TRAVEL BUDGET ANALYSIS =====

Converted Amount: 25500.0
Conversion Fee: 510.0
Total Expense: 26010.0

Converted Amount: 9000.0
Conversion Fee: 90.0
Total Expense: 9090.0

Converted Amount: 12750.0
Conversion Fee: 255.0
Total Expense: 13005.0

Converted Amount: 18000.0
Conversion Fee: 180.0
Total Expense: 18180.0

===== FINAL TRAVEL REPORT =====
Home Currency: INR
Travel Budget: 100000.0
Total Spending: 66285.0

Category-wise Expenses:
Hotel : 26010.0 INR
Food : 9090.0 INR
Transport : 13005.0 INR
Shopping : 18180.0 INR

Largest Expense Category: Hotel
Largest Expense: 26010.0 INR

Status: Within Budget
Remaining Budget: 33715.0

===== THANK YOU =====
```

## 7. Mermaid Flowchart Code

\#chatgpt-mermaid-\_r_bl\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_bl\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_bl\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_bl\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_bl\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bl\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_bl\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_bl\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_bl\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_bl\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_bl\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_bl\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bl\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bl\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_bl\_ p{margin:0;}#chatgpt-mermaid-\_r_bl\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bl\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bl\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bl\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_bl\_ .label text,#chatgpt-mermaid-\_r_bl\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bl\_ .node rect,#chatgpt-mermaid-\_r_bl\_ .node circle,#chatgpt-mermaid-\_r_bl\_ .node ellipse,#chatgpt-mermaid-\_r_bl\_ .node polygon,#chatgpt-mermaid-\_r_bl\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_bl\_ .rough-node .label text,#chatgpt-mermaid-\_r_bl\_ .node .label text,#chatgpt-mermaid-\_r_bl\_ .image-shape .label,#chatgpt-mermaid-\_r_bl\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_bl\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_bl\_ .rough-node .label,#chatgpt-mermaid-\_r_bl\_ .node .label,#chatgpt-mermaid-\_r_bl\_ .image-shape .label,#chatgpt-mermaid-\_r_bl\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_bl\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_bl\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bl\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bl\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_bl\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_bl\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_bl\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_bl\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_bl\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_bl\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_bl\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bl\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bl\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_bl\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bl\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_bl\_ .icon-shape,#chatgpt-mermaid-\_r_bl\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_bl\_ .icon-shape p,#chatgpt-mermaid-\_r_bl\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_bl\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_bl\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_bl\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_bl\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_bl\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_bl\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_bl\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_bl\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_bl\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bl\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_bl\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bl\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_bl\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_bl\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_bl\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_bl\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_bl\_ .node rect,#chatgpt-mermaid-\_r_bl\_ .node circle,#chatgpt-mermaid-\_r_bl\_ .node ellipse,#chatgpt-mermaid-\_r_bl\_ .node polygon,#chatgpt-mermaid-\_r_bl\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_bl\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_bl\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_bl\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_bl\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bl\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter home currency andbudgetEnter number of expensecategoriesInitialize total spending = 0Enter category, currency,amount, rate and feeCalculate converted amountCalculate conversion feeCalculate total expenseAdd expense to category andtotal spendingMore expenses?Find largest expense categoryTotal spending Budget?Calculate excess amountCalculate remaining budgetDisplay final travel reportStopYesNoYesNo

## 8. Expected Result

- Converts expenses from multiple currencies into INR.
- Calculates currency conversion fees.
- Displays category-wise expenses.
- Identifies the largest expense category.
- Checks whether the travel budget is exceeded or within limits.
- Displays the remaining budget.

Note: The exchange rates in the sample input are assumed values for demonstration. The program uses the exchange rates supplied by the user.
