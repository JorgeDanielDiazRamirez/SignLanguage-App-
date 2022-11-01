const {Firestore} = require('@google-cloud/firestore');
const path = require('path');

class FirestoreClient {
    constructor() {
            this.firestore = new Firestore({
                projectId: 'asl-machinelearning-367219',
                keyFilename: path.join(__dirname, './asl-machinelearning-367219-35441f41c58b.json')
            })
        }
        //Building the reference
    async save(collection, data) {
            const docRef = this.firestore.collection(collection).doc(data.docName);
            await docRef.set(data);
        }
        //Awaiting the reference 
    async saveSubCollection(rootCol, rootDocName, subCol, subColData) {
        const docRef = this.firestore.collection(rootCol).doc(rootDocName).collection(subCol).doc(subColData.docName);
        await docRef.set(subColData);
    }

    async saveByPath(path, data) {
        const docRef = this.firestore.doc(path);
        await docRef.set(data);
    }
}

module.exports = new FirestoreClient();