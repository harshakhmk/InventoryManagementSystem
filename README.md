# InventoryManagementAPI

**This API supports two kinds of users**  <br />
### Employee functionalities
-1)View available list of equipments <br />
-2) Issue & Return a particular piece of equipment to the manager <br />
-3)Request access for an unissued equipment <br />

### Manager functionalities
-1)View available/issued pieces of equipments <br />
-2) View access requests by employees<br />

**API Endpoints**  <br />
``` employee/available-equipments ```   <br />
```employee/send-access-requests/<int:id> ```  <br />
```employee/issues-and-return/<int:id> ```   <br />
```manager/available-equipments  ```   <br />
``` manager/issued-equipments  ```   <br />
```manager/view-access-requests```   <br />



