import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('C:\Users\SPM\Downloads\work-automations-4664b-firebase-adminsdk-fbsvc-752623064b.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Reference to your collection in Firestore
accounts_ref = db.collection('accounts')
