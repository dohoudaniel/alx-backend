import chai from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const expect = chai.expect;

// Create a Kue queue for testing
const testQueue = kue.createQueue();

// Set up the Kue test mode before running tests
before(function (done) {
  testQueue.testMode.enter();
  done();
});

// Clean up the Kue test mode after running tests
after(function (done) {
  testQueue.testMode.clear();
  testQueue.testMode.exit();
  done();
});

describe('createPushNotificationsJobs', function () {
  it('should display an error message if jobs is not an array', function () {
    // Arrange
    const invalidJobs = 'This is not an array';

    // Act and Assert
    expect(() => createPushNotificationsJobs(invalidJobs, testQueue)).to.throw('Jobs is not an array');
  });

  it('should create new jobs in the queue', function () {
    // Arrange
    const validJobs = [
      { title: 'Job 1', data: { /* job data */ } },
      { title: 'Job 2', data: { /* job data */ } },
    ];

    // Act
    createPushNotificationsJobs(validJobs, testQueue);

    // Assert
    // Use Kue's test mode to check the jobs in the queue
    const jobs = testQueue.testMode.jobs;
    expect(jobs).to.have.lengthOf(2); // Ensure two jobs were added
    expect(jobs[0].type).to.equal(''); // Check the job type
    expect(jobs[1].type).to.equal('');
    // Additional assertions as needed for job data, job state, etc.
  });
});

