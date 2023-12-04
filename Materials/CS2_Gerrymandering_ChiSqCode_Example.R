VA_current_lightred = (22656 + 6440)/(22656 + 6440 + 9561 + 13372 + 21524 + 5743 + 8387 + 1361 +180)
VA_current_mediumred = 9561/(22656 + 6440 + 9561 + 13372 + 21524 + 5743 + 8387 + 1361 +180)
VA_current_darkred = (13372 + 21524)/(22656 + 6440 + 9561 + 13372 + 21524 + 5743 + 8387 + 1361 +180)
VA_current_purple = 5743/(22656 + 6440 + 9561 + 13372 + 21524 + 5743 + 8387 + 1361 +180)
VA_current_lightblue = 8387/(22656 + 6440 + 9561 + 13372 + 21524 + 5743 + 8387 + 1361 +180)
VA_current_darkblue = (1361 + 180)/(22656 + 6440 + 9561 + 13372 + 21524 + 5743 + 8387 + 1361 +180)

VA_current <- as.data.frame(cbind(VA_current_lightred, VA_current_mediumred, VA_current_darkred, VA_current_purple, VA_current_lightblue, VA_current_darkblue))
VA_current <- VA_current*(22656 + 6440 + 9561 + 13372 + 21524 + 5743 + 8387 + 1361 +180)

rownames(VA_current) <- c("Current")
colnames(VA_current) <- c("Light red", "Medium red", "Dark red", "purple", "Light blue", "Dark blue")

VA_prop_part_lightred = 9229 / (9229 + 10612 + 14907 + 19476 + 21534 + 5474 + 514 + 207 +489 +7501 + 891)
VA_prop_part_mediumred = 0 / (9229 + 10612 + 14907 + 19476 + 21534 + 5474 + 514 + 207 +489 +7501 + 891)
VA_prop_part_darkred = (10612 + 14907 + 19476 + 21534) / (9229 + 10612 + 14907 + 19476 + 21534 + 5474 + 514 + 207 +489 +7501 + 891)
VA_prop_part_purple = 5474 / (9229 + 10612 + 14907 + 19476 + 21534 + 5474 + 514 + 207 +489 +7501 + 891)
VA_prop_part_lightblue = (514 + 207 + 489) / (9229 + 10612 + 14907 + 19476 + 21534 + 5474 + 514 + 207 +489 +7501 + 891)
VA_prop_part_darkblue = (7501 + 891)/(9229 + 10612 + 14907 + 19476 + 21534 + 5474 + 514 + 207 +489 +7501 + 891)

VA_prop_part <- as.data.frame(cbind(VA_prop_part_lightred, VA_prop_part_mediumred, VA_prop_part_darkred, VA_prop_part_purple, VA_prop_part_lightblue, VA_prop_part_darkblue))
VA_prop_part <- VA_prop_part*(9229 + 10612 + 14907 + 19476 + 21534 + 5474 + 514 + 207 +489 +7501 + 891)

rownames(VA_prop_part) <- c("Non-gerrymandered")
colnames(VA_prop_part) <- c("Light red", "Medium red", "Dark red", "purple", "Light blue", "Dark blue")
VA_table <- rbind(VA_current, VA_prop_part)

chisq.test(VA_table)


