# Retail Billing with Multiple Discount Rules using Python

## 1. Problem Statement

Develop a Python program to generate a retail shopping bill for multiple products. The program should calculate the total price based on product quantity, apply category-specific taxes, provide discounts based on purchase amount, and enforce a maximum discount limit.

The program should perform the following operations:

1. Accept multiple product names, categories, prices, and quantities.
2. Calculate the total price of each product.
3. Apply category-specific taxes.
4. Apply threshold-based discounts depending on the total purchase amount.
5. Apply a maximum discount limit.
6. Calculate the final bill amount.
7. Generate an itemized invoice showing product details, taxes, discounts, and total payable amount.

## 2. Algorithm

1. Start the program.
2. Initialize the total purchase amount to zero.
3. Enter the number of products.
4. For each product:
   - Enter product name.
   - Enter product category.
   - Enter product price.
   - Enter product quantity.
5. Calculate the subtotal for each product.

`Subtotal = Price × Quantity`

6. Calculate category-specific tax:
   - Electronics: 18%
   - Clothing: 5%
   - Groceries: 2%
   - Others: 12%
7. Calculate the total amount before discount.
8. Apply threshold-based discounts:
   - Purchase amount above ₹5,000: 10% discount.
   - Purchase amount above ₹3,000: 7% discount.
   - Purchase amount above ₹1,000: 5% discount.
   - Otherwise: No discount.
9. Apply a maximum discount limit of ₹1,000.
10. Calculate the final payable amount.
11. Display the itemized invoice.
12. Stop the program.

## 3. Flowchart


```
 
flowchart TD
    A([Start]) --> B[/Enter number of products/]
    B --> C[Initialize subtotal and tax]
    C --> D[/Enter product name, category, price and quantity/]
    D --> E{Valid price and quantity?}
    E -->|No| F[Display invalid input]
    F --> Z([Stop])
    E -->|Yes| G[Calculate product subtotal]
    G --> H[Identify product category]
    H --> I[Calculate category-specific tax]
    I --> J[Add subtotal and tax to totals]
    J --> K{More products?}
    K -->|Yes| D
    K -->|No| L[Calculate grand total]
    L --> M{Grand total > 5000?}
    M -->|Yes| N[Apply 10% discount]
    M -->|No| O{Grand total > 3000?}
    O -->|Yes| P[Apply 7% discount]
    O -->|No| Q{Grand total > 1000?}
    Q -->|Yes| R[Apply 5% discount]
    Q -->|No| S[No discount]
    N --> T[Check maximum discount limit]
    P --> T
    R --> T
    S --> T
    T --> U[Calculate final payable amount]
    U --> V[Generate itemized invoice]
    V --> W([Stop])
  
```

## 5. Sample Input

```
===================================
       RETAIL BILLING SYSTEM
===================================

Enter number of products: 3

Product 1
Enter product name: Laptop
Enter category: electronics
Enter product price: 40000
Enter quantity: 1

Product 2
Enter product name: Shirt
Enter category: clothing
Enter product price: 1000
Enter quantity: 2

Product 3
Enter product name: Rice
Enter category: groceries
Enter product price: 500
Enter quantity: 2
```

## 6. Sample Output

```
==============================================
              RETAIL INVOICE
==============================================

Product Details:

Product         Category        Price    Qty  Subtotal
----------------------------------------------------------------------
Laptop          electronics  40000.00      1  40000.00
Shirt           clothing      1000.00      2   2000.00
Rice            groceries      500.00      2   1000.00
----------------------------------------------------------------------

Subtotal Amount: Rs. 43000.0
Total Tax:       Rs. 7250.0
Amount Before Discount: Rs. 50250.0

Discount Rate: 10 %
Discount Amount: Rs. 1000
Maximum Discount: Rs. 1000

----------------------------------------------
FINAL PAYABLE AMOUNT: Rs. 49250.0
==============================================

Thank you for shopping!
```

## 7. Mermaid Flowchart Code

Copy the following code into the Mermaid editor to generate your flowchart.

\#chatgpt-mermaid-\_r_jg\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_jg\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_jg\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_jg\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_jg\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_jg\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_jg\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_jg\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_jg\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_jg\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_jg\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_jg\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_jg\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_jg\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_jg\_ p{margin:0;}#chatgpt-mermaid-\_r_jg\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_jg\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_jg\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_jg\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_jg\_ .label text,#chatgpt-mermaid-\_r_jg\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_jg\_ .node rect,#chatgpt-mermaid-\_r_jg\_ .node circle,#chatgpt-mermaid-\_r_jg\_ .node ellipse,#chatgpt-mermaid-\_r_jg\_ .node polygon,#chatgpt-mermaid-\_r_jg\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_jg\_ .rough-node .label text,#chatgpt-mermaid-\_r_jg\_ .node .label text,#chatgpt-mermaid-\_r_jg\_ .image-shape .label,#chatgpt-mermaid-\_r_jg\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_jg\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_jg\_ .rough-node .label,#chatgpt-mermaid-\_r_jg\_ .node .label,#chatgpt-mermaid-\_r_jg\_ .image-shape .label,#chatgpt-mermaid-\_r_jg\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_jg\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_jg\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_jg\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_jg\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_jg\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_jg\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_jg\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_jg\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_jg\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_jg\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_jg\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_jg\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_jg\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_jg\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_jg\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_jg\_ .icon-shape,#chatgpt-mermaid-\_r_jg\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_jg\_ .icon-shape p,#chatgpt-mermaid-\_r_jg\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_jg\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_jg\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_jg\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_jg\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_jg\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_jg\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_jg\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_jg\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_jg\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_jg\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_jg\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_jg\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_jg\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_jg\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_jg\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_jg\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_jg\_ .node rect,#chatgpt-mermaid-\_r_jg\_ .node circle,#chatgpt-mermaid-\_r_jg\_ .node ellipse,#chatgpt-mermaid-\_r_jg\_ .node polygon,#chatgpt-mermaid-\_r_jg\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_jg\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_jg\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_jg\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_jg\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_jg\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of productsInitialize subtotal and taxEnter product name, category,price and quantityValid price and quantity?Display invalid inputStopCalculate product subtotalIdentify product categoryCalculate category-specific taxAdd subtotal and tax to totalsMore products?Calculate grand totalGrand total 5000?Apply 10% discountGrand total 3000?Apply 7% discountGrand total 1000?Apply 5% discountNo discountCheck maximum discount limitCalculate final payable amountGenerate itemized invoiceStopNoYesYesNoYesNoYesNoYesNo

## 8. Python Concepts Used

| Concept              | Purpose                           |
| -------------------- | --------------------------------- |
| Variables            | Store product and billing details |
| Dictionary           | Store category tax rates          |
| For loop             | Process multiple products         |
| If-Else              | Apply discount conditions         |
| List                 | Store product information         |
| Arithmetic operators | Calculate tax and discounts       |
| String formatting    | Display the invoice               |

Note: The tax rates and discount rules in this program are assumed values for an educational project, not actual tax advice.

Project Title: Retail Billing with Multiple Discount Rules using Python.
