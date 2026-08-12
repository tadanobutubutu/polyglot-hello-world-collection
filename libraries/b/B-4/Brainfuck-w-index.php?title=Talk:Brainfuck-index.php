(define interpret-code
  '(cond
    ((null? p) (cons before after))
    ((list? (car p))
     (if (= (car after) 0)
         (interpret (cdr p) before after)
         (let ((result (interpret (car p) before after)))
           (interpret p (car result) (cdr result)))))
    (else
     (case (car p)
       ('+ (interpret (cdr p) before (cons (+ (car after) 1) (cdr after))))
       ('- (interpret (cdr p) before (cons (- (car after) 1) (cdr after))))
       ('< (interpret (cdr p) (cdr before) (cons (car before) after)))
       ('> (interpret (cdr p) (cons (car after) before) (cdr after)))))))

(define (interpret p before after)
  ((eval
   `(letrec ((interpret (lambda (p before after) ,interpret-code)))
      interpret)
   (interaction-environment))
   p before after))

(define (run p)
  (let ((zeroes (list 0)))
    (set-cdr! zeroes zeroes)
    (if (H 0
           `(letrec ((interpret (lambda (p before after) ,interpret-code))
                     (zeroes (list 0)))
              (set-cdr! zeroes zeroes)
              (interpret ',p '() zeroes)))
        (interpret p '() zeroes)
        (error "That's no program!"))))
