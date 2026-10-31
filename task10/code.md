# ATM Transaction Sequence Simulation – Python Program

## 1. Problem Statement

Develop a Python program to simulate ATM transactions by processing a sequence of deposits and withdrawals. The program should maintain the available account balance, enforce withdrawal limits, reject invalid transactions, and generate a final transaction summary.

The program should:

1. Accept the initial account balance.
2. Accept the maximum withdrawal limit per transaction.
3. Accept the number of transactions.
4. Process deposits and withdrawals.
5. Validate transaction amounts.
6. Reject withdrawals exceeding the available balance.
7. Reject withdrawals exceeding the transaction limit.
8. Reject invalid transaction types and negative amounts.
9. Calculate the final account balance.
10. Display the total deposits, total withdrawals, successful transactions, rejected transactions, and final balance.

## 2. Algorithm

1. Start the program.
2. Enter the initial account balance.
3. Enter the maximum withdrawal limit.
4. Enter the number of transactions.
5. Initialize:
   - Total deposits = 0
   - Total withdrawals = 0
   - Successful transactions = 0
   - Rejected transactions = 0
6. Repeat for each transaction:
   - Enter transaction type (Deposit or Withdrawal).
   - Enter transaction amount.
7. Check whether the transaction amount is valid.
8. If the transaction is a deposit:
   - Add the amount to the account balance.
   - Update total deposits.
9. If the transaction is a withdrawal:
   - Check the available balance.
   - Check the maximum withdrawal limit.
   - If both conditions are satisfied, subtract the amount from the balance.
   - Otherwise, reject the transaction.
10. Calculate the final account balance.
11. Display the transaction summary.
12. Stop the program.

## 3. Flowchart


```

flowchart TD
    A([Start]) --> B[/Enter initial balance/]
    B --> C[/Enter withdrawal limit and transaction count/]
    C --> D[Initialize counters]
    D --> E[/Enter transaction type and amount/]
    E --> F{Is amount valid?}
    F -- No --> G[Reject transaction]
    F -- Yes --> H{Transaction type?}
    H -- Deposit --> I[Add amount to balance]
    H -- Withdrawal --> J{Amount exceeds withdrawal limit?}
    H -- Invalid --> G
    J -- Yes --> G
    J -- No --> K{Amount exceeds balance?}
    K -- Yes --> G
    K -- No --> L[Subtract amount from balance]
    I --> M[Update transaction counters]
    L --> M
    G --> N[Update rejected counter]
    N --> O{More transactions?}
    M --> O
    O -- Yes --> E
    O -- No --> P[Calculate transaction summary]
    P --> Q[Display final balance and summary]
    Q --> R([Stop])

```

## 5. Sample Input

```
===== ATM TRANSACTION SYSTEM =====

Enter initial account balance: 10000
Enter maximum withdrawal limit: 5000
Enter number of transactions: 5

Transaction 1
Enter transaction type (D/W): D
Enter transaction amount: 3000

Transaction 2
Enter transaction type (D/W): W
Enter transaction amount: 2000

Transaction 3
Enter transaction type (D/W): W
Enter transaction amount: 6000

Transaction 4
Enter transaction type (D/W): W
Enter transaction amount: 12000

Transaction 5
Enter transaction type (D/W): W
Enter transaction amount: 1000
```

## 6. Sample Output

```
===== ATM TRANSACTION SYSTEM =====

Transaction 1
Deposit Successful
Updated Balance: 13000.0

Transaction 2
Withdrawal Successful
Updated Balance: 11000.0

Transaction 3
Transaction Rejected: Withdrawal limit exceeded

Transaction 4
Transaction Rejected: Withdrawal limit exceeded

Transaction 5
Withdrawal Successful
Updated Balance: 10000.0

===== ATM TRANSACTION SUMMARY =====

Total Deposits: 3000.0
Total Withdrawals: 3000.0
Successful Transactions: 3
Rejected Transactions: 2
Final Account Balance: 10000.0

===== THANK YOU FOR USING ATM =====
```

## 7. Mermaid Flowchart Code

\#chatgpt-mermaid-\_r_l2\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_l2\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_l2\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_l2\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_l2\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_l2\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_l2\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_l2\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_l2\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_l2\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_l2\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_l2\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_l2\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_l2\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_l2\_ p{margin:0;}#chatgpt-mermaid-\_r_l2\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_l2\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_l2\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_l2\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_l2\_ .label text,#chatgpt-mermaid-\_r_l2\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_l2\_ .node rect,#chatgpt-mermaid-\_r_l2\_ .node circle,#chatgpt-mermaid-\_r_l2\_ .node ellipse,#chatgpt-mermaid-\_r_l2\_ .node polygon,#chatgpt-mermaid-\_r_l2\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_l2\_ .rough-node .label text,#chatgpt-mermaid-\_r_l2\_ .node .label text,#chatgpt-mermaid-\_r_l2\_ .image-shape .label,#chatgpt-mermaid-\_r_l2\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_l2\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_l2\_ .rough-node .label,#chatgpt-mermaid-\_r_l2\_ .node .label,#chatgpt-mermaid-\_r_l2\_ .image-shape .label,#chatgpt-mermaid-\_r_l2\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_l2\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_l2\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_l2\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_l2\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_l2\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_l2\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_l2\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_l2\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_l2\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_l2\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_l2\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_l2\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_l2\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_l2\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_l2\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_l2\_ .icon-shape,#chatgpt-mermaid-\_r_l2\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_l2\_ .icon-shape p,#chatgpt-mermaid-\_r_l2\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_l2\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_l2\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_l2\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_l2\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_l2\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_l2\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_l2\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_l2\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_l2\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_l2\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_l2\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_l2\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_l2\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_l2\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_l2\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_l2\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_l2\_ .node rect,#chatgpt-mermaid-\_r_l2\_ .node circle,#chatgpt-mermaid-\_r_l2\_ .node ellipse,#chatgpt-mermaid-\_r_l2\_ .node polygon,#chatgpt-mermaid-\_r_l2\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_l2\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_l2\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_l2\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_l2\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_l2\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter initial balanceEnter withdrawal limit andtransaction countInitialize countersEnter transaction type andamountIs amount valid?Reject transactionTransaction type?Add amount to balanceAmount exceeds withdrawallimit?Amount exceeds balance?Subtract amount from balanceUpdate transaction countersUpdate rejected counterMore transactions?Calculate transaction summaryDisplay final balance andsummaryStopNoYesDepositWithdrawalInvalidYesNoYesNoYesNo

## 8. Important Formulas

| Calculation             | Formula                                              |
| ----------------------- | ---------------------------------------------------- |
| Deposit                 | Balance + Deposit Amount                             |
| Withdrawal              | Balance − Withdrawal Amount                          |
| Total Deposits          | Sum of successful deposits                           |
| Total Withdrawals       | Sum of successful withdrawals                        |
| Final Balance           | Initial Balance + Total Deposits − Total Withdrawals |
| Successful Transactions | Number of accepted transactions                      |
| Rejected Transactions   | Number of rejected transactions                      |

## 9. Expected Result

- Processes multiple ATM transactions.
- Maintains the correct account balance.
- Accepts valid deposits and withdrawals.
- Rejects withdrawals exceeding the balance.
- Enforces the maximum withdrawal limit.
- Rejects invalid transaction amounts and types.
- Generates a complete transaction summary.

Note: This is an educational ATM simulation. It does not connect to a real bank account or perform actual money transfers.
