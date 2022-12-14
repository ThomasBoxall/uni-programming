DROP DATABASE dsd_22;

CREATE DATABASE dsd_22;

SELECT COUNT(*) FROM category;
 count
-------
     6
(1 row)

SELECT COUNT(*) FROM cust_order;
 count
-------
   150
(1 row)

SELECT COUNT(*) FROM customer;
 count
-------
    11
(1 row)

SELECT COUNT(*) FROM manifest;
 count
-------
   150
(1 row)

SELECT COUNT(*) FROM product;
 count
-------
   100
(1 row)

SELECT COUNT(*) FROM role;
 count
-------
     5
(1 row)

SELECT COUNT(*) FROM staff;
 count
-------
    10
(1 row)

\d category
                                      Table "public.category"
  Column  |         Type          | Collation | Nullable |                 Default              

----------+-----------------------+-----------+----------+------------------------------------------
 cat_id   | integer               |           | not null | nextval('category_cat_id_seq'::regclass)
 cat_name | character varying(40) |           |          | 
Indexes:
    "category_pkey" PRIMARY KEY, btree (cat_id)
Referenced by:
    TABLE "product" CONSTRAINT "product_prod_cat_fkey" FOREIGN KEY (prod_cat) REFERENCES category(cat_id)

\d cust_order
                                   Table "public.cust_order"
   Column    |  Type   | Collation | Nullable |                     Default
-------------+---------+-----------+----------+-------------------------------------------------
 cust_ord_id | integer |           | not null | nextval('cust_order_cust_ord_id_seq'::regclass)
 staff_id    | integer |           |          | 
 cust_id     | integer |           |          | 
Indexes:
    "cust_order_pkey" PRIMARY KEY, btree (cust_ord_id)
Foreign-key constraints:
    "cust_order_cust_id_fkey" FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
    "cust_order_staff_id_fkey" FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
Referenced by:
    TABLE "manifest" CONSTRAINT "manifest_cust_ord_id_fkey" FOREIGN KEY (cust_ord_id) REFERENCES cust_order(cust_ord_id)

\d customer
                                        Table "public.customer"
   Column   |          Type          | Collation | Nullable |                  Default          

------------+------------------------+-----------+----------+-------------------------------------------
 cust_id    | integer                |           | not null | nextval('customer_cust_id_seq'::regclass)
 cust_fname | character varying(25)  |           | not null |
 cust_lname | character varying(35)  |           | not null |
 addr1      | character varying(50)  |           | not null |
 addr2      | character varying(50)  |           |          |
 town       | character varying(60)  |           | not null |
 postcode   | character(9)           |           | not null |
 email      | character varying(255) |           | not null |
Indexes:
    "customer_pkey" PRIMARY KEY, btree (cust_id)
Referenced by:
    TABLE "cust_order" CONSTRAINT "cust_order_cust_id_fkey" FOREIGN KEY (cust_id) REFERENCES customer(cust_id)

\d manifest
                                   Table "public.manifest"
   Column    |  Type   | Collation | Nullable |                    Default
-------------+---------+-----------+----------+-----------------------------------------------  
 manifest_id | integer |           | not null | nextval('manifest_manifest_id_seq'::regclass)   
 cust_ord_id | integer |           | not null |
 prod_id     | integer |           | not null |
Indexes:
    "manifest_pkey" PRIMARY KEY, btree (manifest_id)
Foreign-key constraints:
    "manifest_cust_ord_id_fkey" FOREIGN KEY (cust_ord_id) REFERENCES cust_order(cust_ord_id)    
    "manifest_prod_id_fkey" FOREIGN KEY (prod_id) REFERENCES product(prod_id)


\d product
                                       Table "public.product"
  Column   |         Type          | Collation | Nullable |                 Default             

-----------+-----------------------+-----------+----------+------------------------------------------
 prod_id   | integer               |           | not null | nextval('product_prod_id_seq'::regclass)
 prod_name | character varying(50) |           | not null |
 prod_cat  | integer               |           | not null |
Indexes:
    "product_pkey" PRIMARY KEY, btree (prod_id)
Foreign-key constraints:
    "product_prod_cat_fkey" FOREIGN KEY (prod_cat) REFERENCES category(cat_id)
Referenced by:
    TABLE "manifest" CONSTRAINT "manifest_prod_id_fkey" FOREIGN KEY (prod_id) REFERENCES product(prod_id)

\d role
                                       Table "public.role"
  Column   |         Type          | Collation | Nullable |                Default              

-----------+-----------------------+-----------+----------+---------------------------------------
 role_id   | integer               |           | not null | nextval('role_role_id_seq'::regclass)
 role_name | character varying(20) |           |          | 
Indexes:
    "role_pkey" PRIMARY KEY, btree (role_id)
Referenced by:
    TABLE "staff" CONSTRAINT "staff_role_fkey" FOREIGN KEY (role) REFERENCES role(role_id)      



\d staff

                                         Table "public.staff"
   Column    |          Type          | Collation | Nullable |                 Default          

-------------+------------------------+-----------+----------+-----------------------------------------
 staff_id    | integer                |           | not null | nextval('staff_staff_id_seq'::regclass)
 staff_fname | character varying(25)  |           | not null | 
 staff_lname | character varying(35)  |           | not null |
 addr1       | character varying(50)  |           | not null |
 addr2       | character varying(50)  |           |          |
 town        | character varying(60)  |           | not null |
 postcode    | character(9)           |           | not null |
 home_email  | character varying(255) |           | not null |
 work_email  | character varying(100) |           | not null |
 role        | integer                |           | not null |
Indexes:
    "staff_pkey" PRIMARY KEY, btree (staff_id)
Foreign-key constraints:
    "staff_role_fkey" FOREIGN KEY (role) REFERENCES role(role_id)
Referenced by:
    TABLE "cust_order" CONSTRAINT "cust_order_staff_id_fkey" FOREIGN KEY (staff_id) REFERENCES staff(staff_id)



-- STUDENT TASKS 2
Select * from product, category;

 prod_id |                    prod_name                     | prod_cat | cat_id |  cat_name     
---------+--------------------------------------------------+----------+--------+-------------  
       1 | Multi-layered multi-tasking initiative           |        2 |      1 | Men's Wear    
       2 | Operative analyzing task-force                   |        1 |      1 | Men's Wear    
       3 | Exclusive client-server array                    |        5 |      1 | Men's Wear    
       4 | Balanced client-server product                   |        6 |      1 | Men's Wear    
       5 | Exclusive background website                     |        5 |      1 | Men's Wear    
       6 | Pre-emptive holistic intranet                    |        6 |      1 | Men's Wear    
       7 | Re-engineered cohesive methodology               |        1 |      1 | Men's Wear    
       8 | Robust directional projection                    |        2 |      1 | Men's Wear    
       9 | Inverse transitional infrastructure              |        4 |      1 | Men's Wear    
      10 | Multi-tiered explicit paradigm                   |        6 |      1 | Men's Wear    
      11 | Re-engineered explicit software                  |        2 |      1 | Men's Wear    
      12 | Cross-platform fresh-thinking core               |        3 |      1 | Men's Wear    
      13 | Diverse neutral emulation                        |        4 |      1 | Men's Wear    
      14 | Up-sized composite challenge                     |        4 |      1 | Men's Wear    
      15 | Intuitive directional complexity                 |        4 |      1 | Men's Wear    
      16 | Universal encompassing conglomeration            |        5 |      1 | Men's Wear    
      17 | Multi-channelled well-modulated analyzer         |        2 |      1 | Men's Wear    
      18 | Re-engineered actuating capability               |        4 |      1 | Men's Wear    
      19 | Public-key interactive encoding                  |        2 |      1 | Men's Wear    
      20 | Monitored asynchronous function                  |        6 |      1 | Men's Wear    
      21 | Proactive methodical data-warehouse              |        4 |      1 | Men's Wear    
      22 | Balanced real-time info-mediaries                |        1 |      1 | Men's Wear    
      23 | Right-sized mission-critical pricing structure   |        6 |      1 | Men's Wear    
      24 | Synergistic homogeneous ability                  |        5 |      1 | Men's Wear    
      25 | Open-source impactful archive                    |        5 |      1 | Men's Wear    
      26 | Realigned 5th generation artificial intelligence |        2 |      1 | Men's Wear    
      27 | Configurable methodical firmware                 |        5 |      1 | Men's Wear    
      28 | Profound optimal encryption                      |        3 |      1 | Men's Wear    
      29 | Vision-oriented user-facing framework            |        2 |      1 | Men's Wear    
      30 | Secured holistic hierarchy                       |        2 |      1 | Men's Wear    
      31 | Assimilated regional instruction set             |        2 |      1 | Men's Wear    
      32 | Business-focused holistic help-desk              |        3 |      1 | Men's Wear    
      33 | Virtual stable Graphic Interface                 |        5 |      1 | Men's Wear    
      34 | Implemented optimizing benchmark                 |        1 |      1 | Men's Wear    
      35 | Adaptive static website                          |        1 |      1 | Men's Wear    
      36 | Virtual impactful success                        |        2 |      1 | Men's Wear    
      37 | Open-architected homogeneous concept             |        6 |      1 | Men's Wear    
      38 | Diverse reciprocal knowledge base                |        1 |      1 | Men's Wear    
      39 | Realigned homogeneous hub                        |        5 |      1 | Men's Wear    
      40 | Switchable tangible product                      |        4 |      1 | Men's Wear    
      41 | Universal global hub                             |        2 |      1 | Men's Wear    
      42 | Enhanced discrete function                       |        4 |      1 | Men's Wear    
      43 | Horizontal asynchronous intranet                 |        4 |      1 | Men's Wear    
      44 | Quality-focused foreground analyzer              |        5 |      1 | Men's Wear    
      45 | Configurable analyzing solution                  |        3 |      1 | Men's Wear    
      46 | Fully-configurable full-range interface          |        6 |      1 | Men's Wear    
      47 | Monitored non-volatile initiative                |        3 |      1 | Men's Wear    
      48 | Pre-emptive next generation infrastructure       |        3 |      1 | Men's Wear    
      49 | Switchable 5th generation parallelism            |        4 |      1 | Men's Wear    
      50 | Adaptive modular approach                        |        2 |      1 | Men's Wear    
      51 | Synergistic zero defect info-mediaries           |        2 |      1 | Men's Wear    
      52 | Persevering empowering customer loyalty          |        3 |      1 | Men's Wear    
      53 | Robust foreground leverage                       |        1 |      1 | Men's Wear    
      54 | Customizable cohesive capacity                   |        6 |      1 | Men's Wear    
      55 | Progressive modular archive                      |        3 |      1 | Men's Wear    
      56 | Reduced fresh-thinking process improvement       |        2 |      1 | Men's Wear    
      57 | Seamless optimal leverage                        |        6 |      1 | Men's Wear    
      58 | Universal exuding protocol                       |        5 |      1 | Men's Wear    
      59 | Realigned client-driven database                 |        6 |      1 | Men's Wear    
      60 | Balanced hybrid portal                           |        5 |      1 | Men's Wear    
      61 | Customizable well-modulated encryption           |        5 |      1 | Men's Wear    
      62 | Cross-group reciprocal firmware                  |        3 |      1 | Men's Wear    
      63 | 4th generation Graphical User Interface          |        4 |      1 | Men's Wear    
      64 | Business-focused solution-oriented moratorium    |        5 |      1 | Men's Wear    
      65 | Synergistic scalable capability                  |        5 |      1 | Men's Wear    
      66 | Distributed uniform Graphic Interface            |        5 |      1 | Men's Wear    
      67 | Stand-alone composite Graphical User Interface   |        2 |      1 | Men's Wear    
      68 | Future-proofed leading edge customer loyalty     |        4 |      1 | Men's Wear    
      69 | Profound human-resource forecast                 |        6 |      1 | Men's Wear    
      70 | Advanced neutral portal                          |        3 |      1 | Men's Wear    
      71 | Customer-focused needs-based protocol            |        3 |      1 | Men's Wear    
      72 | User-friendly encompassing array                 |        6 |      1 | Men's Wear    
      73 | Decentralized human-resource infrastructure      |        2 |      1 | Men's Wear    
      74 | Balanced modular website                         |        2 |      1 | Men's Wear    
      75 | Horizontal explicit benchmark                    |        2 |      1 | Men's Wear    
      76 | Re-engineered 24/7 knowledge base                |        1 |      1 | Men's Wear    
      77 | Innovative web-enabled extranet                  |        2 |      1 | Men's Wear    
      78 | Exclusive analyzing open architecture            |        2 |      1 | Men's Wear    
      79 | Fundamental global archive                       |        3 |      1 | Men's Wear    
      80 | Profound value-added intranet                    |        5 |      1 | Men's Wear    
      81 | Networked global open system                     |        6 |      1 | Men's Wear    
      82 | Persistent demand-driven complexity              |        5 |      1 | Men's Wear    
      83 | Focused secondary initiative                     |        5 |      1 | Men's Wear    
      84 | Digitized tertiary groupware                     |        3 |      1 | Men's Wear    
      85 | Enhanced homogeneous paradigm                    |        4 |      1 | Men's Wear    
      86 | Inverse high-level attitude                      |        4 |      1 | Men's Wear    
      87 | Quality-focused upward-trending throughput       |        4 |      1 | Men's Wear    
      88 | Team-oriented stable project                     |        6 |      1 | Men's Wear    
      89 | Total intangible artificial intelligence         |        3 |      1 | Men's Wear    
      90 | Streamlined asynchronous functionalities         |        5 |      1 | Men's Wear    
      91 | Vision-oriented attitude-oriented core           |        5 |      1 | Men's Wear    
      92 | Integrated 24/7 interface                        |        2 |      1 | Men's Wear    
      93 | Advanced didactic Graphic Interface              |        1 |      1 | Men's Wear    
      94 | Exclusive multimedia middleware                  |        6 |      1 | Men's Wear    
      95 | Ameliorated next generation orchestration        |        6 |      1 | Men's Wear    
      96 | Front-line demand-driven utilisation             |        5 |      1 | Men's Wear    
      97 | Organic clear-thinking system engine             |        3 |      1 | Men's Wear    
      98 | Persistent incremental model                     |        3 |      1 | Men's Wear    
      99 | Ergonomic solution-oriented local area network   |        2 |      1 | Men's Wear    
     100 | Robust mission-critical complexity               |        5 |      1 | Men's Wear    
       1 | Multi-layered multi-tasking initiative           |        2 |      2 | Ladies Wear   
       2 | Operative analyzing task-force                   |        1 |      2 | Ladies Wear   
       3 | Exclusive client-server array                    |        5 |      2 | Ladies Wear   
       4 | Balanced client-server product                   |        6 |      2 | Ladies Wear   
       5 | Exclusive background website                     |        5 |      2 | Ladies Wear   
       6 | Pre-emptive holistic intranet                    |        6 |      2 | Ladies Wear   
       7 | Re-engineered cohesive methodology               |        1 |      2 | Ladies Wear   
       8 | Robust directional projection                    |        2 |      2 | Ladies Wear   
       9 | Inverse transitional infrastructure              |        4 |      2 | Ladies Wear   
      10 | Multi-tiered explicit paradigm                   |        6 |      2 | Ladies Wear   
      11 | Re-engineered explicit software                  |        2 |      2 | Ladies Wear   
      12 | Cross-platform fresh-thinking core               |        3 |      2 | Ladies Wear   
      13 | Diverse neutral emulation                        |        4 |      2 | Ladies Wear   
      14 | Up-sized composite challenge                     |        4 |      2 | Ladies Wear   
      15 | Intuitive directional complexity                 |        4 |      2 | Ladies Wear   
      16 | Universal encompassing conglomeration            |        5 |      2 | Ladies Wear   
      17 | Multi-channelled well-modulated analyzer         |        2 |      2 | Ladies Wear   
      18 | Re-engineered actuating capability               |        4 |      2 | Ladies Wear   
      19 | Public-key interactive encoding                  |        2 |      2 | Ladies Wear   
      20 | Monitored asynchronous function                  |        6 |      2 | Ladies Wear   
      21 | Proactive methodical data-warehouse              |        4 |      2 | Ladies Wear   
      22 | Balanced real-time info-mediaries                |        1 |      2 | Ladies Wear   
      23 | Right-sized mission-critical pricing structure   |        6 |      2 | Ladies Wear   
      24 | Synergistic homogeneous ability                  |        5 |      2 | Ladies Wear   
      25 | Open-source impactful archive                    |        5 |      2 | Ladies Wear   
      26 | Realigned 5th generation artificial intelligence |        2 |      2 | Ladies Wear   
      27 | Configurable methodical firmware                 |        5 |      2 | Ladies Wear   
      28 | Profound optimal encryption                      |        3 |      2 | Ladies Wear   
      29 | Vision-oriented user-facing framework            |        2 |      2 | Ladies Wear   
      30 | Secured holistic hierarchy                       |        2 |      2 | Ladies Wear   
      31 | Assimilated regional instruction set             |        2 |      2 | Ladies Wear   
      32 | Business-focused holistic help-desk              |        3 |      2 | Ladies Wear   
      33 | Virtual stable Graphic Interface                 |        5 |      2 | Ladies Wear   
      34 | Implemented optimizing benchmark                 |        1 |      2 | Ladies Wear   
      35 | Adaptive static website                          |        1 |      2 | Ladies Wear   
      36 | Virtual impactful success                        |        2 |      2 | Ladies Wear   
      37 | Open-architected homogeneous concept             |        6 |      2 | Ladies Wear   
      38 | Diverse reciprocal knowledge base                |        1 |      2 | Ladies Wear   
      39 | Realigned homogeneous hub                        |        5 |      2 | Ladies Wear   
      40 | Switchable tangible product                      |        4 |      2 | Ladies Wear   
      41 | Universal global hub                             |        2 |      2 | Ladies Wear   
      42 | Enhanced discrete function                       |        4 |      2 | Ladies Wear   
      43 | Horizontal asynchronous intranet                 |        4 |      2 | Ladies Wear   
      44 | Quality-focused foreground analyzer              |        5 |      2 | Ladies Wear   
      45 | Configurable analyzing solution                  |        3 |      2 | Ladies Wear   
      46 | Fully-configurable full-range interface          |        6 |      2 | Ladies Wear   
      47 | Monitored non-volatile initiative                |        3 |      2 | Ladies Wear   
      48 | Pre-emptive next generation infrastructure       |        3 |      2 | Ladies Wear   
      49 | Switchable 5th generation parallelism            |        4 |      2 | Ladies Wear   
      50 | Adaptive modular approach                        |        2 |      2 | Ladies Wear   
      51 | Synergistic zero defect info-mediaries           |        2 |      2 | Ladies Wear   
      52 | Persevering empowering customer loyalty          |        3 |      2 | Ladies Wear   
      53 | Robust foreground leverage                       |        1 |      2 | Ladies Wear   
      54 | Customizable cohesive capacity                   |        6 |      2 | Ladies Wear   
      55 | Progressive modular archive                      |        3 |      2 | Ladies Wear   
      56 | Reduced fresh-thinking process improvement       |        2 |      2 | Ladies Wear   
      57 | Seamless optimal leverage                        |        6 |      2 | Ladies Wear   
      58 | Universal exuding protocol                       |        5 |      2 | Ladies Wear   
      59 | Realigned client-driven database                 |        6 |      2 | Ladies Wear   
      60 | Balanced hybrid portal                           |        5 |      2 | Ladies Wear   
      61 | Customizable well-modulated encryption           |        5 |      2 | Ladies Wear   
      62 | Cross-group reciprocal firmware                  |        3 |      2 | Ladies Wear   
      63 | 4th generation Graphical User Interface          |        4 |      2 | Ladies Wear   
      64 | Business-focused solution-oriented moratorium    |        5 |      2 | Ladies Wear   
      65 | Synergistic scalable capability                  |        5 |      2 | Ladies Wear   
      66 | Distributed uniform Graphic Interface            |        5 |      2 | Ladies Wear   
      67 | Stand-alone composite Graphical User Interface   |        2 |      2 | Ladies Wear   
      68 | Future-proofed leading edge customer loyalty     |        4 |      2 | Ladies Wear   
      69 | Profound human-resource forecast                 |        6 |      2 | Ladies Wear   
      70 | Advanced neutral portal                          |        3 |      2 | Ladies Wear   
      71 | Customer-focused needs-based protocol            |        3 |      2 | Ladies Wear   
      72 | User-friendly encompassing array                 |        6 |      2 | Ladies Wear   
      73 | Decentralized human-resource infrastructure      |        2 |      2 | Ladies Wear   
      74 | Balanced modular website                         |        2 |      2 | Ladies Wear   
      75 | Horizontal explicit benchmark                    |        2 |      2 | Ladies Wear   
      76 | Re-engineered 24/7 knowledge base                |        1 |      2 | Ladies Wear   
      77 | Innovative web-enabled extranet                  |        2 |      2 | Ladies Wear   
      78 | Exclusive analyzing open architecture            |        2 |      2 | Ladies Wear   
      79 | Fundamental global archive                       |        3 |      2 | Ladies Wear   
      80 | Profound value-added intranet                    |        5 |      2 | Ladies Wear   
      81 | Networked global open system                     |        6 |      2 | Ladies Wear   
      82 | Persistent demand-driven complexity              |        5 |      2 | Ladies Wear   
      83 | Focused secondary initiative                     |        5 |      2 | Ladies Wear   
      84 | Digitized tertiary groupware                     |        3 |      2 | Ladies Wear   
      85 | Enhanced homogeneous paradigm                    |        4 |      2 | Ladies Wear   
      86 | Inverse high-level attitude                      |        4 |      2 | Ladies Wear   
      87 | Quality-focused upward-trending throughput       |        4 |      2 | Ladies Wear   
      88 | Team-oriented stable project                     |        6 |      2 | Ladies Wear   
      89 | Total intangible artificial intelligence         |        3 |      2 | Ladies Wear   
      90 | Streamlined asynchronous functionalities         |        5 |      2 | Ladies Wear   
      91 | Vision-oriented attitude-oriented core           |        5 |      2 | Ladies Wear   
      92 | Integrated 24/7 interface                        |        2 |      2 | Ladies Wear   
      93 | Advanced didactic Graphic Interface              |        1 |      2 | Ladies Wear   
      94 | Exclusive multimedia middleware                  |        6 |      2 | Ladies Wear   
      95 | Ameliorated next generation orchestration        |        6 |      2 | Ladies Wear   
      96 | Front-line demand-driven utilisation             |        5 |      2 | Ladies Wear   
      97 | Organic clear-thinking system engine             |        3 |      2 | Ladies Wear   
      98 | Persistent incremental model                     |        3 |      2 | Ladies Wear   
      99 | Ergonomic solution-oriented local area network   |        2 |      2 | Ladies Wear   
     100 | Robust mission-critical complexity               |        5 |      2 | Ladies Wear   
       1 | Multi-layered multi-tasking initiative           |        2 |      3 | Kid's Wear    
       2 | Operative analyzing task-force                   |        1 |      3 | Kid's Wear    
       3 | Exclusive client-server array                    |        5 |      3 | Kid's Wear    
       4 | Balanced client-server product                   |        6 |      3 | Kid's Wear    
       5 | Exclusive background website                     |        5 |      3 | Kid's Wear    
       6 | Pre-emptive holistic intranet                    |        6 |      3 | Kid's Wear    
       7 | Re-engineered cohesive methodology               |        1 |      3 | Kid's Wear    
       8 | Robust directional projection                    |        2 |      3 | Kid's Wear    
       9 | Inverse transitional infrastructure              |        4 |      3 | Kid's Wear    
      10 | Multi-tiered explicit paradigm                   |        6 |      3 | Kid's Wear    
      11 | Re-engineered explicit software                  |        2 |      3 | Kid's Wear    
      12 | Cross-platform fresh-thinking core               |        3 |      3 | Kid's Wear    
      13 | Diverse neutral emulation                        |        4 |      3 | Kid's Wear    
      14 | Up-sized composite challenge                     |        4 |      3 | Kid's Wear    
      15 | Intuitive directional complexity                 |        4 |      3 | Kid's Wear    
      16 | Universal encompassing conglomeration            |        5 |      3 | Kid's Wear    
      17 | Multi-channelled well-modulated analyzer         |        2 |      3 | Kid's Wear    
      18 | Re-engineered actuating capability               |        4 |      3 | Kid's Wear    
      19 | Public-key interactive encoding                  |        2 |      3 | Kid's Wear    
      20 | Monitored asynchronous function                  |        6 |      3 | Kid's Wear    
      21 | Proactive methodical data-warehouse              |        4 |      3 | Kid's Wear    
      22 | Balanced real-time info-mediaries                |        1 |      3 | Kid's Wear    
      23 | Right-sized mission-critical pricing structure   |        6 |      3 | Kid's Wear    
      24 | Synergistic homogeneous ability                  |        5 |      3 | Kid's Wear    
      25 | Open-source impactful archive                    |        5 |      3 | Kid's Wear    
      26 | Realigned 5th generation artificial intelligence |        2 |      3 | Kid's Wear    
      27 | Configurable methodical firmware                 |        5 |      3 | Kid's Wear    
      28 | Profound optimal encryption                      |        3 |      3 | Kid's Wear    
      29 | Vision-oriented user-facing framework            |        2 |      3 | Kid's Wear    
      30 | Secured holistic hierarchy                       |        2 |      3 | Kid's Wear    
      31 | Assimilated regional instruction set             |        2 |      3 | Kid's Wear    
      32 | Business-focused holistic help-desk              |        3 |      3 | Kid's Wear    
      33 | Virtual stable Graphic Interface                 |        5 |      3 | Kid's Wear    
      34 | Implemented optimizing benchmark                 |        1 |      3 | Kid's Wear    
      35 | Adaptive static website                          |        1 |      3 | Kid's Wear    
      36 | Virtual impactful success                        |        2 |      3 | Kid's Wear    
      37 | Open-architected homogeneous concept             |        6 |      3 | Kid's Wear    
      38 | Diverse reciprocal knowledge base                |        1 |      3 | Kid's Wear    
      39 | Realigned homogeneous hub                        |        5 |      3 | Kid's Wear    
      40 | Switchable tangible product                      |        4 |      3 | Kid's Wear    
      41 | Universal global hub                             |        2 |      3 | Kid's Wear    
      42 | Enhanced discrete function                       |        4 |      3 | Kid's Wear    
      43 | Horizontal asynchronous intranet                 |        4 |      3 | Kid's Wear    
      44 | Quality-focused foreground analyzer              |        5 |      3 | Kid's Wear    
      45 | Configurable analyzing solution                  |        3 |      3 | Kid's Wear    
      46 | Fully-configurable full-range interface          |        6 |      3 | Kid's Wear    
      47 | Monitored non-volatile initiative                |        3 |      3 | Kid's Wear    
      48 | Pre-emptive next generation infrastructure       |        3 |      3 | Kid's Wear    
      49 | Switchable 5th generation parallelism            |        4 |      3 | Kid's Wear    
      50 | Adaptive modular approach                        |        2 |      3 | Kid's Wear    
      51 | Synergistic zero defect info-mediaries           |        2 |      3 | Kid's Wear    
      52 | Persevering empowering customer loyalty          |        3 |      3 | Kid's Wear    
      53 | Robust foreground leverage                       |        1 |      3 | Kid's Wear    
      54 | Customizable cohesive capacity                   |        6 |      3 | Kid's Wear    
      55 | Progressive modular archive                      |        3 |      3 | Kid's Wear    
      56 | Reduced fresh-thinking process improvement       |        2 |      3 | Kid's Wear    
      57 | Seamless optimal leverage                        |        6 |      3 | Kid's Wear    
      58 | Universal exuding protocol                       |        5 |      3 | Kid's Wear    
      59 | Realigned client-driven database                 |        6 |      3 | Kid's Wear    
      60 | Balanced hybrid portal                           |        5 |      3 | Kid's Wear    
      61 | Customizable well-modulated encryption           |        5 |      3 | Kid's Wear    
      62 | Cross-group reciprocal firmware                  |        3 |      3 | Kid's Wear    
      63 | 4th generation Graphical User Interface          |        4 |      3 | Kid's Wear    
      64 | Business-focused solution-oriented moratorium    |        5 |      3 | Kid's Wear    
      65 | Synergistic scalable capability                  |        5 |      3 | Kid's Wear    
      66 | Distributed uniform Graphic Interface            |        5 |      3 | Kid's Wear    
      67 | Stand-alone composite Graphical User Interface   |        2 |      3 | Kid's Wear    
      68 | Future-proofed leading edge customer loyalty     |        4 |      3 | Kid's Wear    
      69 | Profound human-resource forecast                 |        6 |      3 | Kid's Wear    
      70 | Advanced neutral portal                          |        3 |      3 | Kid's Wear    
      71 | Customer-focused needs-based protocol            |        3 |      3 | Kid's Wear    
      72 | User-friendly encompassing array                 |        6 |      3 | Kid's Wear    
      73 | Decentralized human-resource infrastructure      |        2 |      3 | Kid's Wear    
      74 | Balanced modular website                         |        2 |      3 | Kid's Wear    
      75 | Horizontal explicit benchmark                    |        2 |      3 | Kid's Wear    
      76 | Re-engineered 24/7 knowledge base                |        1 |      3 | Kid's Wear    
      77 | Innovative web-enabled extranet                  |        2 |      3 | Kid's Wear    
      78 | Exclusive analyzing open architecture            |        2 |      3 | Kid's Wear    
      79 | Fundamental global archive                       |        3 |      3 | Kid's Wear    
      80 | Profound value-added intranet                    |        5 |      3 | Kid's Wear    
      81 | Networked global open system                     |        6 |      3 | Kid's Wear    
      82 | Persistent demand-driven complexity              |        5 |      3 | Kid's Wear    
      83 | Focused secondary initiative                     |        5 |      3 | Kid's Wear    
      84 | Digitized tertiary groupware                     |        3 |      3 | Kid's Wear    
      85 | Enhanced homogeneous paradigm                    |        4 |      3 | Kid's Wear    
      86 | Inverse high-level attitude                      |        4 |      3 | Kid's Wear    
      87 | Quality-focused upward-trending throughput       |        4 |      3 | Kid's Wear    
      88 | Team-oriented stable project                     |        6 |      3 | Kid's Wear    
      89 | Total intangible artificial intelligence         |        3 |      3 | Kid's Wear    
      90 | Streamlined asynchronous functionalities         |        5 |      3 | Kid's Wear    
      91 | Vision-oriented attitude-oriented core           |        5 |      3 | Kid's Wear    
      92 | Integrated 24/7 interface                        |        2 |      3 | Kid's Wear    
      93 | Advanced didactic Graphic Interface              |        1 |      3 | Kid's Wear    
      94 | Exclusive multimedia middleware                  |        6 |      3 | Kid's Wear    
      95 | Ameliorated next generation orchestration        |        6 |      3 | Kid's Wear    
      96 | Front-line demand-driven utilisation             |        5 |      3 | Kid's Wear    
      97 | Organic clear-thinking system engine             |        3 |      3 | Kid's Wear    
      98 | Persistent incremental model                     |        3 |      3 | Kid's Wear    
      99 | Ergonomic solution-oriented local area network   |        2 |      3 | Kid's Wear    
     100 | Robust mission-critical complexity               |        5 |      3 | Kid's Wear    
       1 | Multi-layered multi-tasking initiative           |        2 |      4 | Outdoor       
       2 | Operative analyzing task-force                   |        1 |      4 | Outdoor       
       3 | Exclusive client-server array                    |        5 |      4 | Outdoor       
       4 | Balanced client-server product                   |        6 |      4 | Outdoor       
       5 | Exclusive background website                     |        5 |      4 | Outdoor       
       6 | Pre-emptive holistic intranet                    |        6 |      4 | Outdoor       
       7 | Re-engineered cohesive methodology               |        1 |      4 | Outdoor       
       8 | Robust directional projection                    |        2 |      4 | Outdoor       
       9 | Inverse transitional infrastructure              |        4 |      4 | Outdoor       
      10 | Multi-tiered explicit paradigm                   |        6 |      4 | Outdoor       
      11 | Re-engineered explicit software                  |        2 |      4 | Outdoor       
      12 | Cross-platform fresh-thinking core               |        3 |      4 | Outdoor       
      13 | Diverse neutral emulation                        |        4 |      4 | Outdoor       
      14 | Up-sized composite challenge                     |        4 |      4 | Outdoor       
      15 | Intuitive directional complexity                 |        4 |      4 | Outdoor       
      16 | Universal encompassing conglomeration            |        5 |      4 | Outdoor       
      17 | Multi-channelled well-modulated analyzer         |        2 |      4 | Outdoor       
      18 | Re-engineered actuating capability               |        4 |      4 | Outdoor       
      19 | Public-key interactive encoding                  |        2 |      4 | Outdoor       
      20 | Monitored asynchronous function                  |        6 |      4 | Outdoor       
      21 | Proactive methodical data-warehouse              |        4 |      4 | Outdoor       
      22 | Balanced real-time info-mediaries                |        1 |      4 | Outdoor       
      23 | Right-sized mission-critical pricing structure   |        6 |      4 | Outdoor       
      24 | Synergistic homogeneous ability                  |        5 |      4 | Outdoor       
      25 | Open-source impactful archive                    |        5 |      4 | Outdoor       
      26 | Realigned 5th generation artificial intelligence |        2 |      4 | Outdoor       
      27 | Configurable methodical firmware                 |        5 |      4 | Outdoor       
      28 | Profound optimal encryption                      |        3 |      4 | Outdoor       
      29 | Vision-oriented user-facing framework            |        2 |      4 | Outdoor       
      30 | Secured holistic hierarchy                       |        2 |      4 | Outdoor       
      31 | Assimilated regional instruction set             |        2 |      4 | Outdoor       
      32 | Business-focused holistic help-desk              |        3 |      4 | Outdoor       
      33 | Virtual stable Graphic Interface                 |        5 |      4 | Outdoor       
      34 | Implemented optimizing benchmark                 |        1 |      4 | Outdoor       
      35 | Adaptive static website                          |        1 |      4 | Outdoor       
      36 | Virtual impactful success                        |        2 |      4 | Outdoor       
      37 | Open-architected homogeneous concept             |        6 |      4 | Outdoor       
      38 | Diverse reciprocal knowledge base                |        1 |      4 | Outdoor       
      39 | Realigned homogeneous hub                        |        5 |      4 | Outdoor       
      40 | Switchable tangible product                      |        4 |      4 | Outdoor       
      41 | Universal global hub                             |        2 |      4 | Outdoor       
      42 | Enhanced discrete function                       |        4 |      4 | Outdoor       
      43 | Horizontal asynchronous intranet                 |        4 |      4 | Outdoor       
      44 | Quality-focused foreground analyzer              |        5 |      4 | Outdoor       
      45 | Configurable analyzing solution                  |        3 |      4 | Outdoor       
      46 | Fully-configurable full-range interface          |        6 |      4 | Outdoor       
      47 | Monitored non-volatile initiative                |        3 |      4 | Outdoor       
      48 | Pre-emptive next generation infrastructure       |        3 |      4 | Outdoor       
      49 | Switchable 5th generation parallelism            |        4 |      4 | Outdoor       
      50 | Adaptive modular approach                        |        2 |      4 | Outdoor       
      51 | Synergistic zero defect info-mediaries           |        2 |      4 | Outdoor       
      52 | Persevering empowering customer loyalty          |        3 |      4 | Outdoor       
      53 | Robust foreground leverage                       |        1 |      4 | Outdoor       
      54 | Customizable cohesive capacity                   |        6 |      4 | Outdoor       
      55 | Progressive modular archive                      |        3 |      4 | Outdoor       
      56 | Reduced fresh-thinking process improvement       |        2 |      4 | Outdoor       
      57 | Seamless optimal leverage                        |        6 |      4 | Outdoor       
      58 | Universal exuding protocol                       |        5 |      4 | Outdoor       
      59 | Realigned client-driven database                 |        6 |      4 | Outdoor       
      60 | Balanced hybrid portal                           |        5 |      4 | Outdoor       
      61 | Customizable well-modulated encryption           |        5 |      4 | Outdoor       
      62 | Cross-group reciprocal firmware                  |        3 |      4 | Outdoor       
      63 | 4th generation Graphical User Interface          |        4 |      4 | Outdoor       
      64 | Business-focused solution-oriented moratorium    |        5 |      4 | Outdoor       
      65 | Synergistic scalable capability                  |        5 |      4 | Outdoor       
      66 | Distributed uniform Graphic Interface            |        5 |      4 | Outdoor       
      67 | Stand-alone composite Graphical User Interface   |        2 |      4 | Outdoor       
      68 | Future-proofed leading edge customer loyalty     |        4 |      4 | Outdoor       
      69 | Profound human-resource forecast                 |        6 |      4 | Outdoor       
      70 | Advanced neutral portal                          |        3 |      4 | Outdoor       
      71 | Customer-focused needs-based protocol            |        3 |      4 | Outdoor       
      72 | User-friendly encompassing array                 |        6 |      4 | Outdoor       
      73 | Decentralized human-resource infrastructure      |        2 |      4 | Outdoor       
      74 | Balanced modular website                         |        2 |      4 | Outdoor       
      75 | Horizontal explicit benchmark                    |        2 |      4 | Outdoor       
      76 | Re-engineered 24/7 knowledge base                |        1 |      4 | Outdoor       
      77 | Innovative web-enabled extranet                  |        2 |      4 | Outdoor       
      78 | Exclusive analyzing open architecture            |        2 |      4 | Outdoor       
      79 | Fundamental global archive                       |        3 |      4 | Outdoor       
      80 | Profound value-added intranet                    |        5 |      4 | Outdoor       
      81 | Networked global open system                     |        6 |      4 | Outdoor       
      82 | Persistent demand-driven complexity              |        5 |      4 | Outdoor       
      83 | Focused secondary initiative                     |        5 |      4 | Outdoor       
      84 | Digitized tertiary groupware                     |        3 |      4 | Outdoor       
      85 | Enhanced homogeneous paradigm                    |        4 |      4 | Outdoor       
      86 | Inverse high-level attitude                      |        4 |      4 | Outdoor       
      87 | Quality-focused upward-trending throughput       |        4 |      4 | Outdoor       
      88 | Team-oriented stable project                     |        6 |      4 | Outdoor       
      89 | Total intangible artificial intelligence         |        3 |      4 | Outdoor       
      90 | Streamlined asynchronous functionalities         |        5 |      4 | Outdoor       
      91 | Vision-oriented attitude-oriented core           |        5 |      4 | Outdoor       
      92 | Integrated 24/7 interface                        |        2 |      4 | Outdoor       
      93 | Advanced didactic Graphic Interface              |        1 |      4 | Outdoor       
      94 | Exclusive multimedia middleware                  |        6 |      4 | Outdoor       
      95 | Ameliorated next generation orchestration        |        6 |      4 | Outdoor       
      96 | Front-line demand-driven utilisation             |        5 |      4 | Outdoor       
      97 | Organic clear-thinking system engine             |        3 |      4 | Outdoor       
      98 | Persistent incremental model                     |        3 |      4 | Outdoor       
      99 | Ergonomic solution-oriented local area network   |        2 |      4 | Outdoor       
     100 | Robust mission-critical complexity               |        5 |      4 | Outdoor       
       1 | Multi-layered multi-tasking initiative           |        2 |      5 | Sport
       2 | Operative analyzing task-force                   |        1 |      5 | Sport
       3 | Exclusive client-server array                    |        5 |      5 | Sport
       4 | Balanced client-server product                   |        6 |      5 | Sport
       5 | Exclusive background website                     |        5 |      5 | Sport
       6 | Pre-emptive holistic intranet                    |        6 |      5 | Sport
       7 | Re-engineered cohesive methodology               |        1 |      5 | Sport
       8 | Robust directional projection                    |        2 |      5 | Sport
       9 | Inverse transitional infrastructure              |        4 |      5 | Sport
      10 | Multi-tiered explicit paradigm                   |        6 |      5 | Sport
      11 | Re-engineered explicit software                  |        2 |      5 | Sport
      12 | Cross-platform fresh-thinking core               |        3 |      5 | Sport
      13 | Diverse neutral emulation                        |        4 |      5 | Sport
      14 | Up-sized composite challenge                     |        4 |      5 | Sport
      15 | Intuitive directional complexity                 |        4 |      5 | Sport
      16 | Universal encompassing conglomeration            |        5 |      5 | Sport
      17 | Multi-channelled well-modulated analyzer         |        2 |      5 | Sport
      18 | Re-engineered actuating capability               |        4 |      5 | Sport
      19 | Public-key interactive encoding                  |        2 |      5 | Sport
      20 | Monitored asynchronous function                  |        6 |      5 | Sport
      21 | Proactive methodical data-warehouse              |        4 |      5 | Sport
      22 | Balanced real-time info-mediaries                |        1 |      5 | Sport
      23 | Right-sized mission-critical pricing structure   |        6 |      5 | Sport
      24 | Synergistic homogeneous ability                  |        5 |      5 | Sport
      25 | Open-source impactful archive                    |        5 |      5 | Sport
      26 | Realigned 5th generation artificial intelligence |        2 |      5 | Sport
      27 | Configurable methodical firmware                 |        5 |      5 | Sport
      28 | Profound optimal encryption                      |        3 |      5 | Sport
      29 | Vision-oriented user-facing framework            |        2 |      5 | Sport
      30 | Secured holistic hierarchy                       |        2 |      5 | Sport
      31 | Assimilated regional instruction set             |        2 |      5 | Sport
      32 | Business-focused holistic help-desk              |        3 |      5 | Sport
      33 | Virtual stable Graphic Interface                 |        5 |      5 | Sport
      34 | Implemented optimizing benchmark                 |        1 |      5 | Sport
      35 | Adaptive static website                          |        1 |      5 | Sport
      36 | Virtual impactful success                        |        2 |      5 | Sport
      37 | Open-architected homogeneous concept             |        6 |      5 | Sport
      38 | Diverse reciprocal knowledge base                |        1 |      5 | Sport
      39 | Realigned homogeneous hub                        |        5 |      5 | Sport
      40 | Switchable tangible product                      |        4 |      5 | Sport
      41 | Universal global hub                             |        2 |      5 | Sport
      42 | Enhanced discrete function                       |        4 |      5 | Sport
      43 | Horizontal asynchronous intranet                 |        4 |      5 | Sport
      44 | Quality-focused foreground analyzer              |        5 |      5 | Sport
      45 | Configurable analyzing solution                  |        3 |      5 | Sport
      46 | Fully-configurable full-range interface          |        6 |      5 | Sport
      47 | Monitored non-volatile initiative                |        3 |      5 | Sport
      48 | Pre-emptive next generation infrastructure       |        3 |      5 | Sport
      49 | Switchable 5th generation parallelism            |        4 |      5 | Sport
      50 | Adaptive modular approach                        |        2 |      5 | Sport
      51 | Synergistic zero defect info-mediaries           |        2 |      5 | Sport
      52 | Persevering empowering customer loyalty          |        3 |      5 | Sport
      53 | Robust foreground leverage                       |        1 |      5 | Sport
      54 | Customizable cohesive capacity                   |        6 |      5 | Sport
      55 | Progressive modular archive                      |        3 |      5 | Sport
      56 | Reduced fresh-thinking process improvement       |        2 |      5 | Sport
      57 | Seamless optimal leverage                        |        6 |      5 | Sport
      58 | Universal exuding protocol                       |        5 |      5 | Sport
      59 | Realigned client-driven database                 |        6 |      5 | Sport
      60 | Balanced hybrid portal                           |        5 |      5 | Sport
      61 | Customizable well-modulated encryption           |        5 |      5 | Sport
      62 | Cross-group reciprocal firmware                  |        3 |      5 | Sport
      63 | 4th generation Graphical User Interface          |        4 |      5 | Sport
      64 | Business-focused solution-oriented moratorium    |        5 |      5 | Sport
      65 | Synergistic scalable capability                  |        5 |      5 | Sport
      66 | Distributed uniform Graphic Interface            |        5 |      5 | Sport
      67 | Stand-alone composite Graphical User Interface   |        2 |      5 | Sport
      68 | Future-proofed leading edge customer loyalty     |        4 |      5 | Sport
      69 | Profound human-resource forecast                 |        6 |      5 | Sport
      70 | Advanced neutral portal                          |        3 |      5 | Sport
      71 | Customer-focused needs-based protocol            |        3 |      5 | Sport
      72 | User-friendly encompassing array                 |        6 |      5 | Sport
      73 | Decentralized human-resource infrastructure      |        2 |      5 | Sport
      74 | Balanced modular website                         |        2 |      5 | Sport
      75 | Horizontal explicit benchmark                    |        2 |      5 | Sport
      76 | Re-engineered 24/7 knowledge base                |        1 |      5 | Sport
      77 | Innovative web-enabled extranet                  |        2 |      5 | Sport
      78 | Exclusive analyzing open architecture            |        2 |      5 | Sport
      79 | Fundamental global archive                       |        3 |      5 | Sport
      80 | Profound value-added intranet                    |        5 |      5 | Sport
      81 | Networked global open system                     |        6 |      5 | Sport
      82 | Persistent demand-driven complexity              |        5 |      5 | Sport
      83 | Focused secondary initiative                     |        5 |      5 | Sport
      84 | Digitized tertiary groupware                     |        3 |      5 | Sport
      85 | Enhanced homogeneous paradigm                    |        4 |      5 | Sport
      86 | Inverse high-level attitude                      |        4 |      5 | Sport
      87 | Quality-focused upward-trending throughput       |        4 |      5 | Sport
      88 | Team-oriented stable project                     |        6 |      5 | Sport
      89 | Total intangible artificial intelligence         |        3 |      5 | Sport
      90 | Streamlined asynchronous functionalities         |        5 |      5 | Sport
      91 | Vision-oriented attitude-oriented core           |        5 |      5 | Sport
      92 | Integrated 24/7 interface                        |        2 |      5 | Sport
      93 | Advanced didactic Graphic Interface              |        1 |      5 | Sport
      94 | Exclusive multimedia middleware                  |        6 |      5 | Sport
      95 | Ameliorated next generation orchestration        |        6 |      5 | Sport
      96 | Front-line demand-driven utilisation             |        5 |      5 | Sport
      97 | Organic clear-thinking system engine             |        3 |      5 | Sport
      98 | Persistent incremental model                     |        3 |      5 | Sport
      99 | Ergonomic solution-oriented local area network   |        2 |      5 | Sport
     100 | Robust mission-critical complexity               |        5 |      5 | Sport
       1 | Multi-layered multi-tasking initiative           |        2 |      6 | Health        
       2 | Operative analyzing task-force                   |        1 |      6 | Health        
       3 | Exclusive client-server array                    |        5 |      6 | Health        
       4 | Balanced client-server product                   |        6 |      6 | Health        
       5 | Exclusive background website                     |        5 |      6 | Health        
       6 | Pre-emptive holistic intranet                    |        6 |      6 | Health        
       7 | Re-engineered cohesive methodology               |        1 |      6 | Health        
       8 | Robust directional projection                    |        2 |      6 | Health        
       9 | Inverse transitional infrastructure              |        4 |      6 | Health        
      10 | Multi-tiered explicit paradigm                   |        6 |      6 | Health        
      11 | Re-engineered explicit software                  |        2 |      6 | Health        
      12 | Cross-platform fresh-thinking core               |        3 |      6 | Health        
      13 | Diverse neutral emulation                        |        4 |      6 | Health        
      14 | Up-sized composite challenge                     |        4 |      6 | Health        
      15 | Intuitive directional complexity                 |        4 |      6 | Health        
      16 | Universal encompassing conglomeration            |        5 |      6 | Health        
      17 | Multi-channelled well-modulated analyzer         |        2 |      6 | Health        
      18 | Re-engineered actuating capability               |        4 |      6 | Health        
      19 | Public-key interactive encoding                  |        2 |      6 | Health        
      20 | Monitored asynchronous function                  |        6 |      6 | Health        
      21 | Proactive methodical data-warehouse              |        4 |      6 | Health        
      22 | Balanced real-time info-mediaries                |        1 |      6 | Health        
      23 | Right-sized mission-critical pricing structure   |        6 |      6 | Health        
      24 | Synergistic homogeneous ability                  |        5 |      6 | Health        
      25 | Open-source impactful archive                    |        5 |      6 | Health        
      26 | Realigned 5th generation artificial intelligence |        2 |      6 | Health        
      27 | Configurable methodical firmware                 |        5 |      6 | Health        
      28 | Profound optimal encryption                      |        3 |      6 | Health        
      29 | Vision-oriented user-facing framework            |        2 |      6 | Health        
      30 | Secured holistic hierarchy                       |        2 |      6 | Health        
      31 | Assimilated regional instruction set             |        2 |      6 | Health        
      32 | Business-focused holistic help-desk              |        3 |      6 | Health        
      33 | Virtual stable Graphic Interface                 |        5 |      6 | Health        
      34 | Implemented optimizing benchmark                 |        1 |      6 | Health        
      35 | Adaptive static website                          |        1 |      6 | Health        
      36 | Virtual impactful success                        |        2 |      6 | Health        
      37 | Open-architected homogeneous concept             |        6 |      6 | Health        
      38 | Diverse reciprocal knowledge base                |        1 |      6 | Health        
      39 | Realigned homogeneous hub                        |        5 |      6 | Health        
      40 | Switchable tangible product                      |        4 |      6 | Health        
      41 | Universal global hub                             |        2 |      6 | Health        
      42 | Enhanced discrete function                       |        4 |      6 | Health        
      43 | Horizontal asynchronous intranet                 |        4 |      6 | Health        
      44 | Quality-focused foreground analyzer              |        5 |      6 | Health        
      45 | Configurable analyzing solution                  |        3 |      6 | Health        
      46 | Fully-configurable full-range interface          |        6 |      6 | Health        
      47 | Monitored non-volatile initiative                |        3 |      6 | Health        
      48 | Pre-emptive next generation infrastructure       |        3 |      6 | Health        
      49 | Switchable 5th generation parallelism            |        4 |      6 | Health        
      50 | Adaptive modular approach                        |        2 |      6 | Health        
      51 | Synergistic zero defect info-mediaries           |        2 |      6 | Health        
      52 | Persevering empowering customer loyalty          |        3 |      6 | Health        
      53 | Robust foreground leverage                       |        1 |      6 | Health        
      54 | Customizable cohesive capacity                   |        6 |      6 | Health        
      55 | Progressive modular archive                      |        3 |      6 | Health        
      56 | Reduced fresh-thinking process improvement       |        2 |      6 | Health        
      57 | Seamless optimal leverage                        |        6 |      6 | Health        
      58 | Universal exuding protocol                       |        5 |      6 | Health        
      59 | Realigned client-driven database                 |        6 |      6 | Health        
      60 | Balanced hybrid portal                           |        5 |      6 | Health        
      61 | Customizable well-modulated encryption           |        5 |      6 | Health        
      62 | Cross-group reciprocal firmware                  |        3 |      6 | Health        
      63 | 4th generation Graphical User Interface          |        4 |      6 | Health        
      64 | Business-focused solution-oriented moratorium    |        5 |      6 | Health        
      65 | Synergistic scalable capability                  |        5 |      6 | Health        
      66 | Distributed uniform Graphic Interface            |        5 |      6 | Health        
      67 | Stand-alone composite Graphical User Interface   |        2 |      6 | Health        
      68 | Future-proofed leading edge customer loyalty     |        4 |      6 | Health        
      69 | Profound human-resource forecast                 |        6 |      6 | Health        
      70 | Advanced neutral portal                          |        3 |      6 | Health        
      71 | Customer-focused needs-based protocol            |        3 |      6 | Health        
      72 | User-friendly encompassing array                 |        6 |      6 | Health        
      73 | Decentralized human-resource infrastructure      |        2 |      6 | Health        
      74 | Balanced modular website                         |        2 |      6 | Health        
      75 | Horizontal explicit benchmark                    |        2 |      6 | Health        
      76 | Re-engineered 24/7 knowledge base                |        1 |      6 | Health        
      77 | Innovative web-enabled extranet                  |        2 |      6 | Health        
      78 | Exclusive analyzing open architecture            |        2 |      6 | Health        
      79 | Fundamental global archive                       |        3 |      6 | Health        
      80 | Profound value-added intranet                    |        5 |      6 | Health        
      81 | Networked global open system                     |        6 |      6 | Health        
      82 | Persistent demand-driven complexity              |        5 |      6 | Health        
      83 | Focused secondary initiative                     |        5 |      6 | Health        
      84 | Digitized tertiary groupware                     |        3 |      6 | Health        
      85 | Enhanced homogeneous paradigm                    |        4 |      6 | Health        
      86 | Inverse high-level attitude                      |        4 |      6 | Health        
      87 | Quality-focused upward-trending throughput       |        4 |      6 | Health        
      88 | Team-oriented stable project                     |        6 |      6 | Health        
      89 | Total intangible artificial intelligence         |        3 |      6 | Health        
      90 | Streamlined asynchronous functionalities         |        5 |      6 | Health        
      91 | Vision-oriented attitude-oriented core           |        5 |      6 | Health        
      92 | Integrated 24/7 interface                        |        2 |      6 | Health        
      93 | Advanced didactic Graphic Interface              |        1 |      6 | Health        
      94 | Exclusive multimedia middleware                  |        6 |      6 | Health        
      95 | Ameliorated next generation orchestration        |        6 |      6 | Health        
      96 | Front-line demand-driven utilisation             |        5 |      6 | Health        
      97 | Organic clear-thinking system engine             |        3 |      6 | Health        
      98 | Persistent incremental model                     |        3 |      6 | Health        
      99 | Ergonomic solution-oriented local area network   |        2 |      6 | Health        
     100 | Robust mission-critical complexity               |        5 |      6 | Health        
(600 rows)

select * from category, product where prod_name = 'Multi-layered multi-tasking initiative';
 cat_id |  cat_name   | prod_id |               prod_name                | prod_cat
--------+-------------+---------+----------------------------------------+----------
      1 | Men's Wear  |       1 | Multi-layered multi-tasking initiative |        2
      2 | Ladies Wear |       1 | Multi-layered multi-tasking initiative |        2
      3 | Kid's Wear  |       1 | Multi-layered multi-tasking initiative |        2
      4 | Outdoor     |       1 | Multi-layered multi-tasking initiative |        2
      5 | Sport       |       1 | Multi-layered multi-tasking initiative |        2
      6 | Health      |       1 | Multi-layered multi-tasking initiative |        2
(6 rows)


select * from category
join product on category.cat_id = product.prod_cat;
 cat_id |  cat_name   | prod_id |                    prod_name                     | prod_cat   
--------+-------------+---------+--------------------------------------------------+----------  
      2 | Ladies Wear |       1 | Multi-layered multi-tasking initiative           |        2   
      1 | Men's Wear  |       2 | Operative analyzing task-force                   |        1   
      5 | Sport       |       3 | Exclusive client-server array                    |        5
      6 | Health      |       4 | Balanced client-server product                   |        6   
      5 | Sport       |       5 | Exclusive background website                     |        5   
      6 | Health      |       6 | Pre-emptive holistic intranet                    |        6   
      1 | Men's Wear  |       7 | Re-engineered cohesive methodology               |        1   
      2 | Ladies Wear |       8 | Robust directional projection                    |        2   
      4 | Outdoor     |       9 | Inverse transitional infrastructure              |        4   
      6 | Health      |      10 | Multi-tiered explicit paradigm                   |        6   
      2 | Ladies Wear |      11 | Re-engineered explicit software                  |        2   
      3 | Kid's Wear  |      12 | Cross-platform fresh-thinking core               |        3   
      4 | Outdoor     |      13 | Diverse neutral emulation                        |        4   
      4 | Outdoor     |      14 | Up-sized composite challenge                     |        4   
      4 | Outdoor     |      15 | Intuitive directional complexity                 |        4   
      5 | Sport       |      16 | Universal encompassing conglomeration            |        5   
      2 | Ladies Wear |      17 | Multi-channelled well-modulated analyzer         |        2   
      4 | Outdoor     |      18 | Re-engineered actuating capability               |        4   
      2 | Ladies Wear |      19 | Public-key interactive encoding                  |        2   
      6 | Health      |      20 | Monitored asynchronous function                  |        6   
      4 | Outdoor     |      21 | Proactive methodical data-warehouse              |        4   
      1 | Men's Wear  |      22 | Balanced real-time info-mediaries                |        1   
      6 | Health      |      23 | Right-sized mission-critical pricing structure   |        6   
      5 | Sport       |      24 | Synergistic homogeneous ability                  |        5   
      5 | Sport       |      25 | Open-source impactful archive                    |        5   
      2 | Ladies Wear |      26 | Realigned 5th generation artificial intelligence |        2   
      5 | Sport       |      27 | Configurable methodical firmware                 |        5   
      3 | Kid's Wear  |      28 | Profound optimal encryption                      |        3   
      2 | Ladies Wear |      29 | Vision-oriented user-facing framework            |        2   
      2 | Ladies Wear |      30 | Secured holistic hierarchy                       |        2   
      2 | Ladies Wear |      31 | Assimilated regional instruction set             |        2   
      3 | Kid's Wear  |      32 | Business-focused holistic help-desk              |        3   
      5 | Sport       |      33 | Virtual stable Graphic Interface                 |        5   
      1 | Men's Wear  |      34 | Implemented optimizing benchmark                 |        1   
      1 | Men's Wear  |      35 | Adaptive static website                          |        1   
      2 | Ladies Wear |      36 | Virtual impactful success                        |        2   
      6 | Health      |      37 | Open-architected homogeneous concept             |        6   
      1 | Men's Wear  |      38 | Diverse reciprocal knowledge base                |        1   
      5 | Sport       |      39 | Realigned homogeneous hub                        |        5   
      4 | Outdoor     |      40 | Switchable tangible product                      |        4   
      2 | Ladies Wear |      41 | Universal global hub                             |        2   
      4 | Outdoor     |      42 | Enhanced discrete function                       |        4   
      4 | Outdoor     |      43 | Horizontal asynchronous intranet                 |        4   
      5 | Sport       |      44 | Quality-focused foreground analyzer              |        5   
      3 | Kid's Wear  |      45 | Configurable analyzing solution                  |        3   
      6 | Health      |      46 | Fully-configurable full-range interface          |        6   
      3 | Kid's Wear  |      47 | Monitored non-volatile initiative                |        3   
      3 | Kid's Wear  |      48 | Pre-emptive next generation infrastructure       |        3   
      4 | Outdoor     |      49 | Switchable 5th generation parallelism            |        4   
      2 | Ladies Wear |      50 | Adaptive modular approach                        |        2   
      2 | Ladies Wear |      51 | Synergistic zero defect info-mediaries           |        2   
      3 | Kid's Wear  |      52 | Persevering empowering customer loyalty          |        3   
      1 | Men's Wear  |      53 | Robust foreground leverage                       |        1   
      6 | Health      |      54 | Customizable cohesive capacity                   |        6   
      3 | Kid's Wear  |      55 | Progressive modular archive                      |        3   
      2 | Ladies Wear |      56 | Reduced fresh-thinking process improvement       |        2   
      6 | Health      |      57 | Seamless optimal leverage                        |        6   
      5 | Sport       |      58 | Universal exuding protocol                       |        5   
      6 | Health      |      59 | Realigned client-driven database                 |        6   
      5 | Sport       |      60 | Balanced hybrid portal                           |        5   
      5 | Sport       |      61 | Customizable well-modulated encryption           |        5   
      3 | Kid's Wear  |      62 | Cross-group reciprocal firmware                  |        3   
      4 | Outdoor     |      63 | 4th generation Graphical User Interface          |        4   
      5 | Sport       |      64 | Business-focused solution-oriented moratorium    |        5   
      5 | Sport       |      65 | Synergistic scalable capability                  |        5   
      5 | Sport       |      66 | Distributed uniform Graphic Interface            |        5   
      2 | Ladies Wear |      67 | Stand-alone composite Graphical User Interface   |        2   
      4 | Outdoor     |      68 | Future-proofed leading edge customer loyalty     |        4   
      6 | Health      |      69 | Profound human-resource forecast                 |        6   
      3 | Kid's Wear  |      70 | Advanced neutral portal                          |        3   
      3 | Kid's Wear  |      71 | Customer-focused needs-based protocol            |        3   
      6 | Health      |      72 | User-friendly encompassing array                 |        6   
      2 | Ladies Wear |      73 | Decentralized human-resource infrastructure      |        2   
      2 | Ladies Wear |      74 | Balanced modular website                         |        2   
      2 | Ladies Wear |      75 | Horizontal explicit benchmark                    |        2   
      1 | Men's Wear  |      76 | Re-engineered 24/7 knowledge base                |        1   
      2 | Ladies Wear |      77 | Innovative web-enabled extranet                  |        2   
      2 | Ladies Wear |      78 | Exclusive analyzing open architecture            |        2   
      3 | Kid's Wear  |      79 | Fundamental global archive                       |        3   
      5 | Sport       |      80 | Profound value-added intranet                    |        5   
      6 | Health      |      81 | Networked global open system                     |        6   
      5 | Sport       |      82 | Persistent demand-driven complexity              |        5   
      5 | Sport       |      83 | Focused secondary initiative                     |        5   
      3 | Kid's Wear  |      84 | Digitized tertiary groupware                     |        3   
      4 | Outdoor     |      85 | Enhanced homogeneous paradigm                    |        4   
      4 | Outdoor     |      86 | Inverse high-level attitude                      |        4   
      4 | Outdoor     |      87 | Quality-focused upward-trending throughput       |        4   
      6 | Health      |      88 | Team-oriented stable project                     |        6   
      3 | Kid's Wear  |      89 | Total intangible artificial intelligence         |        3   
      5 | Sport       |      90 | Streamlined asynchronous functionalities         |        5   
      5 | Sport       |      91 | Vision-oriented attitude-oriented core           |        5   
      2 | Ladies Wear |      92 | Integrated 24/7 interface                        |        2   
      1 | Men's Wear  |      93 | Advanced didactic Graphic Interface              |        1   
      6 | Health      |      94 | Exclusive multimedia middleware                  |        6   
      6 | Health      |      95 | Ameliorated next generation orchestration        |        6   
      5 | Sport       |      96 | Front-line demand-driven utilisation             |        5   
      3 | Kid's Wear  |      97 | Organic clear-thinking system engine             |        3   
      3 | Kid's Wear  |      98 | Persistent incremental model                     |        3   
      2 | Ladies Wear |      99 | Ergonomic solution-oriented local area network   |        2   
      5 | Sport       |     100 | Robust mission-critical complexity               |        5   
(100 rows)

'
select * from category
join product on category.cat_id = product.prod_cat
where prod_name = 'Multi-layered multi-tasking initiative';

 cat_id |  cat_name   | prod_id |               prod_name                | prod_cat
--------+-------------+---------+----------------------------------------+----------
      2 | Ladies Wear |       1 | Multi-layered multi-tasking initiative |        2
(1 row)


select count(*) from customer, cust_order;
 count
-------
  1650
(1 row)

select customer.cust_fname, customer.cust_lname, cust_order.cust_ord_id from customer
join cust_order on customer.cust_id = cust_order.cust_id
where cust_order.cust_id = 1;

 cust_fname | cust_lname | cust_ord_id
------------+------------+-------------
 Jobey      | Boeter     |          26
 Jobey      | Boeter     |          34
 Jobey      | Boeter     |          39
 Jobey      | Boeter     |          57
 Jobey      | Boeter     |          68
 Jobey      | Boeter     |          71
 Jobey      | Boeter     |          77
 Jobey      | Boeter     |          91
 Jobey      | Boeter     |          98
 Jobey      | Boeter     |          99
 Jobey      | Boeter     |         131
 Jobey      | Boeter     |         143
 Jobey      | Boeter     |         146
(13 rows)



select customer.cust_fname, customer.cust_lname, cust_order.cust_ord_id, staff.staff_fname, staff.staff_lname from customer
join cust_order on customer.cust_id = cust_order.cust_id
join staff on cust_order.staff_id = staff.staff_id
where cust_order.cust_id = 1;

 cust_fname | cust_lname | cust_ord_id | staff_fname | staff_lname
------------+------------+-------------+-------------+-------------
 Jobey      | Boeter     |          26 | Montgomery  | Housegoe
 Jobey      | Boeter     |          34 | Hanan       | Gloster
 Jobey      | Boeter     |          39 | Hanan       | Gloster
 Jobey      | Boeter     |          57 | Nikoletta   | Shrimpton
 Jobey      | Boeter     |          68 | Montgomery  | Housegoe
 Jobey      | Boeter     |          71 | Nikoletta   | Shrimpton
 Jobey      | Boeter     |          77 | Hanan       | Gloster
 Jobey      | Boeter     |          91 | Niel        | Welsby
 Jobey      | Boeter     |          98 | Montgomery  | Housegoe
 Jobey      | Boeter     |          99 | Janeva      | Gillicuddy
 Jobey      | Boeter     |         131 | Aura        | Clewlowe
 Jobey      | Boeter     |         143 | Janeva      | Gillicuddy
 Jobey      | Boeter     |         146 | Montgomery  | Housegoe
(13 rows)

select role.role_id, role.role_name from role
join staff on role.role_id = staff.role
join cust_order on staff.staff_id = cust_order.staff_id
where cust_order.cust_ord_id = 4;

 role_id | role_name
---------+-----------
       5 | Misc
(1 row)

select customer.cust_fname, customer.cust_lname, cust_order.cust_ord_id, staff.staff_fname, staff.staff_lname, role.role_id, role.role_name from customer
join cust_order on customer.cust_id = cust_order.cust_id
join staff on cust_order.staff_id = staff.staff_id
join role on staff.role = role.role_id
where customer.cust_id = 4;

 cust_fname |    cust_lname    | cust_ord_id | staff_fname | staff_lname | role_id |    role_name
------------+------------------+-------------+-------------+-------------+---------+-----------------
 Chadd      | Franz-Schoninger |           1 | Aura        | Clewlowe    |       3 | Post Sales 
 Chadd      | Franz-Schoninger |           7 | Aura        | Clewlowe    |       3 | Post Sales 
 Chadd      | Franz-Schoninger |          66 | Montgomery  | Housegoe    |       1 | Order Picker
 Chadd      | Franz-Schoninger |          81 | Janeva      | Gillicuddy  |       5 | Misc       
 Chadd      | Franz-Schoninger |          93 | Niel        | Welsby      |       2 | Final Packer
 Chadd      | Franz-Schoninger |          97 | Aura        | Clewlowe    |       3 | Post Sales 
 Chadd      | Franz-Schoninger |         107 | Hanan       | Gloster     |       4 | Customer Retain
 Chadd      | Franz-Schoninger |         109 | Nikoletta   | Shrimpton   |       4 | Customer Retain
 Chadd      | Franz-Schoninger |         124 | Aura        | Clewlowe    |       3 | Post Sales 
 Chadd      | Franz-Schoninger |         129 | Nikoletta   | Shrimpton   |       4 | Customer Retain
(10 rows)