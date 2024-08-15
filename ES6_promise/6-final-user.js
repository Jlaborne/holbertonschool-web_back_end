import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  // Call both functions and get their promises
  const signUpPromise = signUpUser(firstName, lastName);
  const photoUploadPromise = uploadPhoto(fileName);

  // Use Promise.allSettled to handle both promises
  return Promise.allSettled([signUpPromise, photoUploadPromise])
    .then((results) => results.map((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : `Error: ${result.reason.message}`,
    })));
}
