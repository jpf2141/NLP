import nltk


_ITER_ = 10


# TODO: Initialize IBM Model 1 and return the model.
def create_ibm1(aligned_sents):
    ibm1 = nltk.IBMModel1(aligned_sents, _ITER_)
    return ibm1


# TODO: Initialize IBM Model 2 and return the model.
def create_ibm2(aligned_sents):
    ibm2 = nltk.IBMModel2(aligned_sents, _ITER_)
    return ibm2


# TODO: Compute the average AER for the first n sentences
#       in aligned_sents using model. Return the average AER.
def compute_avg_aer(aligned_sents, model, n):
    sent_count = n
    total_error = 0.0
    for sent in aligned_sents[:n]:
        aligned_model = model.align(sent)
        error = sent.alignment_error_rate(aligned_model)
        total_error += error
    avg = total_error/sent_count
    return avg


# TODO: Computes the alignments for the first 20 sentences in
#       aligned_sents and saves the sentences and their alignments
#       to file_name. Use the format specified in the assignment.
def save_model_output(aligned_sents, model, file_name):
    with open(file_name, "w") as file:
        for sent in aligned_sents[:20]:
            aligned_model = model.align(sent)
            line1 = aligned_model.words
            line2 = aligned_model.mots
            line3 = aligned_model.alignment

            file.write(str(line1) + "\n")
            file.write(str(line2) + "\n")
            file.write(str(line3) + "\n\n")


def main(aligned_sents):
    
    ibm1 = create_ibm1(aligned_sents)
    save_model_output(aligned_sents, ibm1, "ibm1.txt")
    avg_aer = compute_avg_aer(aligned_sents, ibm1, 50)

    print ('IBM Model 1')
    print ('---------------------------')
    print('Average AER: {0:.3f}\n'.format(avg_aer))

    ibm2 = create_ibm2(aligned_sents)
    save_model_output(aligned_sents, ibm2, "ibm2.txt")
    avg_aer = compute_avg_aer(aligned_sents, ibm2, 50)
    
    print ('IBM Model 2')
    print ('---------------------------')
    print('Average AER: {0:.3f}\n'.format(avg_aer))



###########################################
#used to calculate optimal iteration counts
###########################################
#def main(aligned_sents):
#    print ('IBM Model 1')
#    for i in range(15):
#        start_time = time.clock()
#        ibm1 = create_ibm1(aligned_sents, i)
#        save_model_output(aligned_sents, ibm1, "ibm1.txt")
#        avg_aer = compute_avg_aer(aligned_sents, ibm1, 50)
#        end_time = time.clock()
#        timer = end_time - start_time
#        timer = str(timer)
#
#
#
#
#        #        print ('IBM Model 1')
#        print "Iterations: " + str(i)
#        print "Time: " + timer
#        #        print ('---------------------------')
#        print('Average AER: {0:.3f}\n'.format(avg_aer))
#
#
#
#    print "\n"
#    print ('IBM Model 2')
#    for i in range(15):
#        start_time = time.clock()
#        ibm2 = create_ibm2(aligned_sents, i)
#        save_model_output(aligned_sents, ibm2, "ibm2.txt")
#        avg_aer = compute_avg_aer(aligned_sents, ibm2, 50)
#        end_time = time.clock()
#        timer = end_time - start_time
#        timer = str(timer)
#
#
#
#        #        print ('IBM Model 2')
#        print "Iterations: " + str(i)
#        print "Time: " + timer
#        #        print ('---------------------------')
#        print('Average AER: {0:.3f}\n'.format(avg_aer))
#
#
#










