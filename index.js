const FirestoreClient = require('./firestoreClient.js');

const data1 = {
    docName: 'label1',
    contentData: 'Metadaata'
};

const save = async() => {
    await FirestoreClient.save('Labels', data1);
}

save();