# Overview

This document highlights steps for suppliers to add staff users to their accounts.

# Suggested Work Flow

- An authorized supplier user creates an invitation to start this process.

- The invitation is stored in an intermediate table (Invitation). This table allows another supplier to invite the same user, however the combination of Email and Supplier (Email, Supplier) is unique together. See Scheme Below:

| Field      | Description                                  |
| ---------- | -------------------------------------------- |
| First Name | Required, non-unique                         |
| Last Name  | Required, non-unique                         |
| Phone      | Required, Allows Duplicates                  |
| Email      | Required, Allows Duplicates                  |
| Supplier   | FK to the Supplier Model                     |
| Status     | Required. One of Pending, Active or Rejected |
|            |                                              |

- If the email address already exists on the system as a user, the user cannot be invited unless the account is deleted. (done)

- The invitation list should be visible to the supplier user, as well as a separate list for staff already invited whom have accepted the invitation. (done)

- If the supplier tries to add the same user he sent an invite earlier, An notification message informs the supplier that the user has already been sent an invite. (done)

- A supplier may copy the invite link from the dashboard and share with the user (FEMI requested). (done)

- The Invitation email gives options for a user to Reject/Accept the invite. The email includes a link which redirects to a page where the user can accept or decline the invitation. (done)

- If the user accepts the invite, he/she is redirected to a page to create a new password for his account. (done)

- On success, the user is graduated to the Custom User table and added to the supplier account he/she accepted the invite from. (done)

- The status of the staff user is set to active on supplier dashboard after a complete handshake. The user is displayed under the linked users under the supplier. It is visible by all supplier users. (done)

- On rejection of the Invite, Supplier is notified of the rejection status via email and status also reflect rejected on the dashboard. (Done)

- The supplier can still reinvite the user by copying the invite link from the dashboard if he/she wish to. (Done)

```
Note: The status of a staff user on the supplier dashboard, in the invitation list, can either be pending, active or rejected.

pending - When a supplier first sends an invite
active -  When a staff user accepts the invite and completes the process
rejected - When user rejects the invite.
```
