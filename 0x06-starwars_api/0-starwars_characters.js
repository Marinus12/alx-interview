#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function getCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body).name);
      } else {
        reject(error);
      }
    });
  });
}

request(url, async function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      try {
        const name = await getCharacterName(character);
        console.log(name);
      } catch (error) {
        console.error(error);
      }
    }
  }
});
