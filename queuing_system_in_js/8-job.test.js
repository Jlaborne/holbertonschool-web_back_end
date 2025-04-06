import { expect } from "chai";
import kue from "kue";
import createPushNotificationsJobs from "./8-job.js";

describe("createPushNotificationsJobs", () => {
  let queue;

  before(() => {
    queue = kue.createQueue();

    // Monkey patch: Add testMode manually if not defined
    if (!queue.testMode) {
      queue.testMode = {
        _jobs: [],
        enter() {
          this._jobs = [];
        },
        clear() {
          this._jobs = [];
        },
        exit() {
          this._jobs = [];
        },
        get jobs() {
          return this._jobs;
        },
        create(type, data) {
          const job = { type, data };
          this._jobs.push(job);
          return {
            type,
            data,
            save(cb) {
              cb && cb();
            },
            on: () => {},
          };
        },
      };
    }

    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("should throw an error if jobs is not an array", () => {
    expect(() => createPushNotificationsJobs("not an array", queue)).to.throw(
      "Jobs is not an array"
    );
  });

  it("should create two new jobs to the queue", () => {
    const jobs = [
      {
        phoneNumber: "1234567890",
        message: "This is the code 1234 to verify your account",
      },
      {
        phoneNumber: "9876543210",
        message: "This is the code 4321 to verify your account",
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    const [job1, job2] = queue.testMode.jobs;

    expect(job1.type).to.equal("push_notification_code_3");
    expect(job1.data).to.deep.equal(jobs[0]);
    expect(job2.data).to.deep.equal(jobs[1]);
  });
});
