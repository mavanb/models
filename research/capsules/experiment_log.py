from experiment_log import *
import tensorflow as tf

def train_experiment(session, result, writer, last_step, max_steps, saver,
                     summary_dir, save_step):
  """Runs training for up to max_steps and saves the model and summaries.

  Args:
    session: The loaded tf.session with the initialized model.
    result: The resultant operations of the model including train_op.
    writer: The summary writer file.
    last_step: The last trained step.
    max_steps: Maximum number of training iterations.
    saver: An instance of tf.train.saver to save the current model.
    summary_dir: The directory to save the model in it.
    save_step: How often to save the model ckpt.
  """
  step = 0
  for i in range(last_step, max_steps):
    print("hoi")
    step += 1
    summary, _ = session.run([result.summary, result.train_op])
    writer.add_summary(summary, i)
    if (i + 1) % save_step == 0:
      saver.save(
          session, os.path.join(summary_dir, 'model.ckpt'), global_step=i + 1)

main = main

if __name__ == '__main__':
  tf.app.run()
