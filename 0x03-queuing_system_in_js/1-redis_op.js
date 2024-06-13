const { createClient } = require('redis');
const client = createClient();

// Listen for errors
client.on('error', err => console.log(`Redis client error: ${err.message}`));
console.log('Redis client connected to the server');

function setNewSchool(schoolName, value){
    client.set(`${schoolName}`, value);
}
function displaySchoolValue(schoolName){
    client.get(`${schoolName}`, (err, value) => {
        if (err) throw err;
        console.log(value);
    });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');